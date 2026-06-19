def find_repeated_letters(input_string):
    letter_count = {}
    for char in input_string:
        if char.isalpha():
            char_lower = char.lower()
            if char_lower in letter_count:
                letter_count[char_lower] += 1
            else:
                letter_count[char_lower] = 1
    
    repeated_letters = {char for char, count in letter_count.items() if count > 1}
    return repeated_letters

if __name__ == '__main__':
    sample_string_1 = "programming"
    result_1 = find_repeated_letters(sample_string_1)
    print(result_1)

    sample_string_2 = "hello world"
    result_2 = find_repeated_letters(sample_string_2)
    print(result_2)

    sample_string_3 = "Alibaba Cloud"
    result_3 = find_repeated_letters(sample_string_3)
    print(result_3)