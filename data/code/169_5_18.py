def calculate_net_change(operations):
    counts = {}
    for operation in operations:
        item, change = operation.split()
        item = item.strip()
        change = int(change)
        if item not in counts:
            counts[item] = 0
        counts[item] += change
        if counts[item] < 0:
            raise ValueError(f"Negative count detected for {item}: {counts[item]}")
    return counts

if __name__ == '__main__':
    operations = [
        "apple +3",
        "banana -2",
        "orange +1",
        "apple -4"
    ]
    try:
        result = calculate_net_change(operations)
        print(result)
    except ValueError as e:
        print(e)