from collections import Counter

def count_items(data):
    return Counter(data)

if __name__ == '__main__':
    sample_list = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
    print(count_items(sample_list))