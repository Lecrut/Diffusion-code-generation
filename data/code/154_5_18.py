def count_frequencies(data):
    freqs = {}
    for item in data:
        freqs[item] = freqs.get(item, 0) + 1
    return freqs

if __name__ == '__main__':
    sample_data = [1, 2, 3, 2, 4, 2, 5, 2]
    frequencies = count_frequencies(sample_data)
    print(frequencies)