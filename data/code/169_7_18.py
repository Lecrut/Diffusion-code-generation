def update_item_counts(transactions):
    frequency_map = {}
    for item in transactions:
        if item in frequency_map:
            frequency_map[item] += 1
        else:
            frequency_map[item] = 1
    return sorted(frequency_map.items())

if __name__ == '__main__':
    sample_transactions = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana']
    print(update_item_counts(sample_transactions))