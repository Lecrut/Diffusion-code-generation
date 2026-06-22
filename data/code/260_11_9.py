MAX_VALUE = float('-inf')

def find_max_in_sets(*sets):
    max_values = {}
    for set_name, numbers in sets:
        if not numbers:
            max_values[set_name] = MAX_VALUE
        else:
            max_values[set_name] = max(numbers)
    return max_values

if __name__ == '__main__':
    sample_sets = [
        ('set1', [3, 5, 2]),
        ('set2', [10, 7, 8, 9]),
        ('set3', []),
        ('set4', [-1, -3, -2])
    ]
    results = find_max_in_sets(*sample_sets)
    for set_name, max_value in results.items():
        print(f"Maximum in {set_name}: {max_value}")