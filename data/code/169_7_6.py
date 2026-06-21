def update_item_counts(transactions):
    counts = {}
    for item in transactions:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    return sorted(counts.items())

if __name__ == '__main__':
    sample_transactions = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana']
    print(update_item_counts(sample_transactions))