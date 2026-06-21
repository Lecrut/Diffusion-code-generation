def find_all_letters(text):
    letters = set()
    in_word = False
    current_word = []
    for char in text:
        if char.isalpha():
            if not in_word:
                in_word = True
            current_word.append(char.lower())
        elif in_word:
            letters.add(''.join(current_word))
            current_word = []
            in_word = False
    if in_word:
        letters.add(''.join(current_word))
    return letters

if __name__ == '__main__':
    sample_string1 = "Hello world! This is a test, with mixed cases."
    sample_string2 = "Python programming is fun; let's see it."
    sample_string3 = "A B C. 123!"
    result1 = find_all_letters(sample_string1)
    print(f"'{sample_string1}' -> {result1}")
    result2 = find_all_letters(sample_string2)
    print(f"'{sample_string2}' -> {result2}")
    result3 = find_all_letters(sample_string3)
    print(f"'{sample_string3}' -> {result3}")