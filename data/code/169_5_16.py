def calculate_net_change(operations):
    counts = {}
    for operation in operations:
        item, change = operation.split()
        if item not in counts:
            counts[item] = 0
        counts[item] += int(change)
        if counts[item] < 0:
            raise ValueError(f"Negative count detected for {item}: {counts[item]}")
    return counts

if __name__ == '__main__':
    operations = [
        "apple +3",
        "banana -2",
        "orange +5",
        "apple -4"
    ]
    try:
        final_counts = calculate_net_change(operations)
        print(final_counts)
    except ValueError as e:
        print(e)