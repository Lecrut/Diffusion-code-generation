def count_frequencies(numbers):
    freq_dict = {}
    for number in numbers:
        if number in freq_dict:
            freq_dict[number] += 1
        else:
            freq_dict[number] = 1
    return sorted(freq_dict.items())

if __name__ == '__main__':
    sample_numbers = [3, 1, 2, 3, 4, 2, 5, 1, 1]
    print(count_frequencies(sample_numbers))