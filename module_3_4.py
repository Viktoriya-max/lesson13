def single_root_words (root_word, *other_words):
    some_words = []
    for i in other_words:
        if root_word.upper() in i.upper() or i.upper() in root_word.upper():
            some_words.append(i)
    return some_words
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
print(result1)
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result2)
