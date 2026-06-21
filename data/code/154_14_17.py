from collections import Counter

def tally_items(sequence):
    return dict(Counter(sequence))
if __name__ == '__main__':
    sample_list = [3, 1, 2, 3, 4, 2, 5]
    result = tally_items(sample_list)
    print(result)