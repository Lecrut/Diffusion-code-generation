def calculate_frequency(items):
    frequency = {}
    for item in items:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1
    return frequency

if __name__ == '__main__':
    sample_items = [1, 2, 3, 4, 5, 1, 2, 1]
    print(calculate_frequency(sample_items))