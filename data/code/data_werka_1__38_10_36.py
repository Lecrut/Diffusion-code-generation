def find_repeated_letters(input_string):
    from collections import Counter
    filtered_chars = [char.lower() for char in input_string if char.isalpha()]
    letter_counts = Counter(filtered_chars)
    repeated_letters = {letter for letter, count in letter_counts.items() if count > 1}
    return repeated_letters
if __name__ == '__main__':
    sample_string_1 = 'programming'
    result_1 = find_repeated_letters(sample_string_1)
    print('Repeated letters in', sample_string_1, ':', result_1)
    sample_string_2 = 'hello world'
    result_2 = find_repeated_letters(sample_string_2)
    print('Repeated letters in', sample_string_2, ':', result_2)