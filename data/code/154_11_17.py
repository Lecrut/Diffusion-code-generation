def calculate_frequency(items):
    frequency = {}
    for item in items:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1
    return frequency

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 2, 3, 2]
    print(f"Frequency of items in {sample_list}: {calculate_frequency(sample_list)}")