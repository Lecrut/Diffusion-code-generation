from collections import Counter

def calculate_frequency(item_list):
    return dict(Counter(item_list))

if __name__ == '__main__':
    inventory_items = ['apple', 'banana', 'orange', 'apple', 'kiwi', 'banana', 'apple']
    frequency_count = calculate_frequency(inventory_items)
    print(frequency_count)