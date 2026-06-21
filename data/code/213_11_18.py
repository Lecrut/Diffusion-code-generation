def count_frequencies(numbers):
    freq_dict = {}
    for number in numbers:
        if number in freq_dict:
            freq_dict[number] += 1
        else:
            freq_dict[number] = 1
    return [(k, v) for k, v in sorted(freq_dict.items())]

if __name__ == '__main__':
    sample_values = [3, 1, 2, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print(count_frequencies(sample_values))