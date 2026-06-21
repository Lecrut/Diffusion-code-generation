def tally_elements(lst):
    freq = {}
    for item in lst:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1
    return freq

if __name__ == '__main__':
    sample_list = [1, 2, 3, 2, 4, 3, 5, 1, 1]
    print(tally_elements(sample_list))