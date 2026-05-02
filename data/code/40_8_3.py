def first_letters(text):
    words = text.split()
    result = []
    for word in words:
        if word and any(char.isalpha() for char in word):
            result.append(word[0])
    return result
if __name__ == '__main__':
    sample1 = "Hello world, this is a test."
    sample2 = "Word1, Word2. Word3---"
    sample3 = "  !@#$  .  "
    sample4 = "Only. Punctuation!  "
    sample5 = "Word1, Word2"
    print(f"'{sample1}': {first_letters(sample1)}")
    print(f"'{sample2}': {first_letters(sample2)}")
    print(f"'{sample3}': {first_letters(sample3)}")
    print(f"'{sample4}': {first_letters(sample4)}")
    print(f"'{sample5}': {first_letters(sample5)}")