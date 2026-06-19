def count_repeated_letters(s):
    letter_count = {}
    for char in s:
        if char.isalpha():
            char_lower = char.lower()
            if char_lower in letter_count:
                letter_count[char_lower] += 1
            else:
                letter_count[char_lower] = 1
    repeated_letters = {char: count for char, count in letter_count.items() if count > 1}
    return repeated_letters
if __name__ == '__main__':
    sample_string = 'Hello World! This is a Test String with some Repeated letters.'
    result = count_repeated_letters(sample_string)
    print(result)