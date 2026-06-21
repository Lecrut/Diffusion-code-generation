def validate_operations(operations):
    for op in operations:
        if not isinstance(op, tuple) or len(op) != 2:
            raise ValueError("Invalid operation format")
        item, count = op
        if not isinstance(item, str) or not isinstance(count, int):
            raise ValueError("Invalid operation values")

def calculate_net_changes(operations):
    validate_operations(operations)
    counts = {}
    for item, count in operations:
        if item in counts:
            counts[item] += count
        else:
            counts[item] = count
    
    negative_counts = {item: count for item, count in counts.items() if count < 0}
    if negative_counts:
        raise ValueError("Negative count detected", negative_counts)
    
    return counts

if __name__ == '__main__':
    operations = [
        ("apple", 1),
        ("banana", -2),
        ("orange", 3),
        ("apple", -1)
    ]
    try:
        result = calculate_net_changes(operations)
        print(result)
    except ValueError as e:
        if isinstance(e.args[0], dict):
            print("Error:", "Negative counts detected")
            for item, count in e.args[0].items():
                print(f"{item}: {count}")
        else:
            print("Error:", e.args[0])