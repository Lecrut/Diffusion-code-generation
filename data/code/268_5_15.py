def find_first_word(text):
    if not text:
        return ''
    i = 0
    while i < len(text) and text[i].isspace():
        i += 1
    if i == len(text):
        return ''
    j = i + 1
    while j < len(text) and (not text[j].isspace()):
        j += 1
    return text[i:j]
if __name__ == '__main__':
    print(find_first_word(''))
    print(find_first_word('   '))
    print(find_first_word('hello world'))
    print(find_first_word('  leading space'))
    print(find_first_word('trailing space '))
    print(find_first_word('singleword'))