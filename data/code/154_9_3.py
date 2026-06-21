def count_frequencies(items):
    if not hasattr(items, '__iter__'):
        raise TypeError("Input is not iterable")
    
    frequency_dict = {}
    for item in items:
        if item in frequency_dict:
            frequency_dict[item] += 1
        else:
            frequency_dict[item] = 1
    
    return frequency_dict

if __name__ == '__main__':
    sample_list = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
    print(count_frequencies(sample_list))