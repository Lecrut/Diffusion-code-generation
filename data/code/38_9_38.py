def find_repeated_letters(input_string):
    letter_count = {}
    repeated_letters = []
    for char in input_string:
        if char.isalpha():
            char_lower = char.lower()
            if char_lower in letter_count:
                letter_count[char_lower] += 1
                if letter_count[char_lower] == 2:
                    repeated_letters.append(char_lower)
            else:
                letter_count[char_lower] = 1
    return repeated_letters
if __name__ == '__main__':
    sample_string = 'This is a simple test string with some repeated letters.'
    result = find_repeated_letters(sample_string)
    print(result)