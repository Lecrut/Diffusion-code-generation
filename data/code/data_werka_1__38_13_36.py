def count_repeated_letters(s):
    letter_count = {}
    repeated_letters = {}
    for char in s:
        if char.isalpha():
            char_lower = char.lower()
            if char_lower in letter_count:
                letter_count[char_lower] += 1
            else:
                letter_count[char_lower] = 1
    for char, count in letter_count.items():
        if count > 1:
            repeated_letters[char] = count
    return repeated_letters
if __name__ == '__main__':
    sample_string = 'Hello World! This is a Test string with some Repeated letters.'
    result = count_repeated_letters(sample_string)
    print(result)