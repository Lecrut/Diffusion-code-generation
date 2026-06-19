def count_repeated_letters(s):
    letter_count = {}
    for char in s:
        if char.isalpha():
            char_lower = char.lower()
            if char_lower in letter_count:
                letter_count[char_lower] += 1
            else:
                letter_count[char_lower] = 1
    return {char: count for char, count in letter_count.items() if count > 1}

if __name__ == '__main__':
    sample_string1 = 'Alibaba Cloud is a great platform'
    sample_string2 = 'Hello World! This is a Test String with some Repeated letters.'
    result1 = count_repeated_letters(sample_string1)
    result2 = count_repeated_letters(sample_string2)
    print(result1)
    print(result2)