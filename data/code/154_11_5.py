def calculate_frequency(items):
    frequency = {}
    for item in items:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1
    return frequency

if __name__ == '__main__':
    sample_list_1 = [1, 2, 3, 4, 5, 2, 3, 1]
    sample_list_2 = ['a', 'b', 'c', 'a']
    print(f"Frequency for {sample_list_1}: {calculate_frequency(sample_list_1)}")
    print(f"Frequency for {sample_list_2}: {calculate_frequency(sample_list_2)}")