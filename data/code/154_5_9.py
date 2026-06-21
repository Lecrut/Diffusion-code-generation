def count_frequencies(data):
    freqs = {}
    for item in data:
        if item not in freqs:
            freqs[item] = 1
        else:
            freqs[item] += 1
    return freqs

if __name__ == '__main__':
    sample_data = ['red', 'blue', 'green', 'red', 'blue', 'red']
    result = count_frequencies(sample_data)
    print(result)