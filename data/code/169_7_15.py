def update_item_counts(transactions):
    item_counts = {}
    for transaction in transactions:
        if transaction in item_counts:
            item_counts[transaction] += 1
        else:
            item_counts[transaction] = 1
    return sorted(item_counts.items())

if __name__ == '__main__':
    transactions = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana']
    print(update_item_counts(transactions))