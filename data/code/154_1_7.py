def tally_frequencies(input_list):
    frequency_dict = {}
    for item in input_list:
        if item in frequency_dict:
            frequency_dict[item] += 1
        else:
            frequency_dict[item] = 1
    return frequency_dict

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 1, 2, 1]
    print(tally_frequencies(sample_list))