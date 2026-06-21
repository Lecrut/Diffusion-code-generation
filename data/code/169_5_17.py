def calculate_net_change(operations):
    item_counts = {}
    for operation in operations:
        item, count = operation.split()
        if item not in item_counts:
            item_counts[item] = 0
        item_counts[item] += int(count)
        if item_counts[item] < 0:
            raise ValueError(f"Negative count detected for {item}: {item_counts[item]}")
    return item_counts

if __name__ == '__main__':
    operations = [
        'apple +5',
        'banana -2',
        'orange +3',
        'apple -10'
    ]
    try:
        final_counts = calculate_net_change(operations)
        print(final_counts)
    except ValueError as e:
        print(e)