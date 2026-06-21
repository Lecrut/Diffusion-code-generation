def item_frequency_counter(items):
    freq_dict = {}
    for item in items:
        if item in freq_dict:
            freq_dict[item] += 1
        else:
            freq_dict[item] = 1
    return freq_dict

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 2, 3, 1]
    print(f"Frequency of items in {sample_list}: {item_frequency_counter(sample_list)}")