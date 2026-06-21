def count_frequencies(numbers):
    if not isinstance(numbers, list) or not all(isinstance(x, int) for x in numbers):
        raise ValueError("Input must be a list of integers")
    
    frequency_dict = {}
    for number in numbers:
        if number in frequency_dict:
            frequency_dict[number] += 1
        else:
            frequency_dict[number] = 1
    
    return sorted(frequency_dict.items())

if __name__ == '__main__':
    sample_numbers = [3, 1, 2, 3, 4, 2, 5, 6, 7, 8, 9, 9]
    print(count_frequencies(sample_numbers))