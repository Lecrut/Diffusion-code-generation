def tally_items(sequence):
    tally = {}
    for item in sequence:
        if item in tally:
            tally[item] += 1
        else:
            tally[item] = 1
    return dict(sorted(tally.items(), key=lambda x: x[1]))
if __name__ == '__main__':
    sample_list = ['apple', 'banana', 'apple', 'orange', 'banana', 'kiwi']
    result = tally_items(sample_list)
    print(result)