def count_frequencies(numbers):
    frequency_dict = {}
    for number in numbers:
        if number in frequency_dict:
            frequency_dict[number] += 1
        else:
            frequency_dict[number] = 1
    return sorted(frequency_dict.items())

if __name__ == '__main__':
    sample_numbers = [3, 1, 2, 3, 4, 2, 5, 1, 3]
    print(count_frequencies(sample_numbers))