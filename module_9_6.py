def all_variants(text):
    for r in range(len(text)):
        for l in range(len(text) - r):
            yield text[l:r + l + 1]


a = all_variants("abc")
for i in a:
    print(i)