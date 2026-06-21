def update_item_counts(transactions):
    count_map = {}
    for item in transactions:
        if item in count_map:
            count_map[item] += 1
        else:
            count_map[item] = 1
    return sorted(count_map.items())

if __name__ == '__main__':
    transactions = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana']
    print(update_item_counts(transactions))