def tally_frequencies(lst):
    freqs = {}
    for item in lst:
        if item in freqs:
            freqs[item] += 1
        else:
            freqs[item] = 1
    return freqs

if __name__ == '__main__':
    sample_list = [1, 2, 3, 2, 1, 4, 5, 4, 4]
    print(tally_frequencies(sample_list))