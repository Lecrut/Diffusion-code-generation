from collections import Counter

def count_items(lst):
    return Counter(lst)

if __name__ == '__main__':
    sample_list = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
    print(count_items(sample_list))