def calculate_net_change(operations):
    counts = {}
    for operation in operations:
        item, amount = operation.split()
        if item not in counts:
            counts[item] = 0
        counts[item] += int(amount)
        if counts[item] < 0:
            raise ValueError(f"Negative count detected for {item}: {counts[item]}")
    return counts

if __name__ == '__main__':
    operations = ["apple +3", "banana -2", "orange +5", "apple -4"]
    print(calculate_net_change(operations))