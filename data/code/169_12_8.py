from collections import Counter

def calculate_item_frequencies(item_list):
    return dict(Counter(item_list))

if __name__ == '__main__':
    item_samples = ['apple', 'banana', 'orange', 'apple', 'kiwi', 'banana', 'apple']
    frequencies = calculate_item_frequencies(item_samples)
    print(frequencies)