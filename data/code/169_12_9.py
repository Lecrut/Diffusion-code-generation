from collections import Counter

def item_frequency_counter(item_list):
    return dict(Counter(item_list))

if __name__ == '__main__':
    sample_items = ['apple', 'banana', 'orange', 'apple', 'kiwi', 'banana', 'apple']
    frequency_count = item_frequency_counter(sample_items)
    print(frequency_count)