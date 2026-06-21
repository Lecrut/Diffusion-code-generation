from collections import Counter

def calculate_item_frequencies(item_list):
    item_counter = Counter()
    for item in item_list:
        item_counter[item] += 1
    return dict(item_counter)

if __name__ == '__main__':
    sample_items = ['apple', 'banana', 'orange', 'grape', 'apple', 'banana']
    frequencies = calculate_item_frequencies(sample_items)
    print(frequencies)