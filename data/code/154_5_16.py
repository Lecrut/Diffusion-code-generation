def count_frequencies(data):
    freqs = {}
    for item in data:
        freqs[item] = freqs.get(item, 0) + 1
    return freqs

if __name__ == '__main__':
    sample_list = ['apple', 'banana', 'cherry', 'date', 'apple', 'banana']
    frequencies = count_frequencies(sample_list)
    for fruit, frequency in frequencies.items():
        print(f"{fruit}: {frequency}")