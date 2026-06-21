def count_frequencies(data):
    freqs = {}
    for item in data:
        freqs[item] = freqs.get(item, 0) + 1
    return freqs

if __name__ == '__main__':
    sample_data = ['red', 'blue', 'green', 'blue', 'red', 'red']
    result = count_frequencies(sample_data)
    print(result)