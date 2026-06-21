def count_frequencies(numbers):
    freq_dict = {}
    for number in numbers:
        if number in freq_dict:
            freq_dict[number] += 1
        else:
            freq_dict[number] = 1
    return sorted(freq_dict.items())

if __name__ == '__main__':
    sample_numbers = [4, 5, 6, 4, 3, 2, 1, 5, 6]
    print(count_frequencies(sample_numbers))