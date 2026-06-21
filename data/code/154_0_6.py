from collections import Counter

def count_items(item_list):
    return Counter(item_list)

if __name__ == '__main__':
    sample_list = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
    print(count_items(sample_list))