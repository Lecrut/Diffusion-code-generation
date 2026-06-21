from collections import Counter

def count_items(item_list):
    return dict(Counter(item_list))

if __name__ == '__main__':
    sample_items = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
    print(count_items(sample_items))