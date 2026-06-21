def count_frequencies(data):
    freqs = {}
    for item in data:
        freqs[item] = freqs.get(item, 0) + 1
    return freqs

if __name__ == '__main__':
    sample_data = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
    result = count_frequencies(sample_data)
    print(result)