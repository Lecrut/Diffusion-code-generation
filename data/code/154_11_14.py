def item_frequency_counter(iterable):
    frequency = {}
    for item in iterable:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1
    return frequency

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 1, 2]
    print(f"Frequency of items in {sample_list}: {item_frequency_counter(sample_list)}")