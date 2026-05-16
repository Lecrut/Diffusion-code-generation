def count_repeated_letters(input_string):
    letter_counts = {}
    for char in input_string:
        if char in letter_counts:
            letter_counts[char] += 1
        else:
            letter_counts[char] = 1
    return letter_counts
if __name__ == '__main__':
    sample_string = "hello world"
    result_dict = count_repeated_letters(sample_string)
    print(result_dict)