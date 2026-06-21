def calculate_net_change(operations):
    item_counts = {}
    for operation in operations:
        item, change = operation.split()
        item_counts[item] = item_counts.get(item, 0) + int(change)
        if item_counts[item] < 0:
            raise ValueError(f"Negative count detected for item: {item}")
    return item_counts

if __name__ == '__main__':
    operations = [
        "apple +2",
        "banana -1",
        "orange +3",
        "apple -5"
    ]
    try:
        final_counts = calculate_net_change(operations)
        print(final_counts)
    except ValueError as e:
        print(e)