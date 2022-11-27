from __future__ import unicode_literals

import stopwordsiso
from hazm import *

normalizer = Normalizer()

#  Digesting Persian text
# see the https://github.com/sobhe/hazm
txt = normalizer.normalize('اصلاح نويسه ها و استفاده از نیم‌فاصله پردازش را آسان مي كند')
txt2 = normalizer.normalize('اصلاح نويسه  ها و استفاده از نیم‌فاصله پردازش را آسان می كند')
X_list = word_tokenize(txt)
X_list2 = word_tokenize(txt2)
stemmer = Stemmer()
lemmatizer = Lemmatizer()
S_list = list(map(stemmer.stem, X_list))
L_list = list(map(lemmatizer.lemmatize, S_list))
S_list2 = list(map(stemmer.stem, X_list2))
L_list2 = list(map(lemmatizer.lemmatize, S_list2))
sw = stopwordsiso.stopwords("fa")

X_set = {w for w in X_list if not w in sw}
X_set2 = {w for w in X_list2 if not w in sw}

# Similarity using cosine
# see the https://biquyetxaynha.com/cosine-similarity-between-two-sentences-python-code
l1 = [];
l2 = []
rvector = X_set.union(X_set2)
for w in rvector:
    if w in X_set:
        l1.append(1)  # create a vector
    else:
        l1.append(0)
    if w in X_set2:
        l2.append(1)
    else:
        l2.append(0)
c = 0

# cosine formula
for i in range(len(rvector)):
    c += l1[i] * l2[i]
cosine = c / float((sum(l1) * sum(l2)) ** 0.5)
print("similarity: ", cosine)
