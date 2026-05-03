def count_repeated_letters(input_string):
    letter_counts = {}
    for char in input_string:
        if char in letter_counts:
            letter_counts[char] += 1
        else:
            letter_counts[char] = 1
    result = {}
    for letter, count in letter_counts.items():
        if count > 1:
            result[letter] = count
    return result
if __name__ == '__main__':
    sample_string = "hello world"
    output_dictionary = count_repeated_letters(sample_string)
    print(output_dictionary)