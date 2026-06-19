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
    sample_string1 = 'Alibaba Cloud'
    sample_string2 = 'Hello World! Hello Universe!'
    sample_string3 = 'Python Programming'
    result1 = count_repeated_letters(sample_string1)
    result2 = count_repeated_letters(sample_string2)
    result3 = count_repeated_letters(sample_string3)
    print(result1)
    print(result2)
    print(result3)