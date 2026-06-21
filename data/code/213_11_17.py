def count_frequencies(numbers):
    if not numbers:
        return []
    
    frequency_dict = {}
    for number in numbers:
        if number in frequency_dict:
            frequency_dict[number] += 1
        else:
            frequency_dict[number] = 1
    
    result = sorted(frequency_dict.items())
    return result

if __name__ == '__main__':
    sample_numbers = [3, 1, 2, 3, 5, 1, 4, 5, 2]
    print(count_frequencies(sample_numbers))