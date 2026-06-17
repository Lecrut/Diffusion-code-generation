def compare_distances(value_a: int | float, value_b: int | float) -> str:
    a = value_a
    b = value_b
    try:
        int_a = int(a)
        int_b = int(b)
        if int_a < int_b:
            return 'less'
        elif int_a > int_b:
            return 'greater'
        else:
            return 'equal'
    except (ValueError, OverflowError):
        if a < b:
            return 'less'
        elif a > b:
            return 'greater'
        else:
            return 'equal'
if __name__ == '__main__':
    sample_a = 1_000_000_000_000_000_000
    sample_b = 987654321.1
    result = compare_distances(sample_a, sample_b)
    print(f"Comparing {sample_a} and {sample_b}:")
    print(result)