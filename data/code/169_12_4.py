from collections import Counter

def tally_items(item_list):
    return dict(Counter(item_list))

if __name__ == '__main__':
    item_samples = ['apple', 'banana', 'orange', 'apple', 'kiwi', 'banana', 'apple']
    item_tally = tally_items(item_samples)
    print(item_tally)