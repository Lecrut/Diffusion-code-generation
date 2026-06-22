def find_the_middle_value_among_three_summary(a, b, c):
    return sorted([a, b, c])[1]

if __name__ == '__main__':
    sample_values = {
        'case1': (3, 1, 2),
        'case2': (10, 5, 20),
        'case3': (10, 25, 15)
    }

    for name, values in sample_values.items():
        result = find_the_middle_value_among_three_summary(*values)
        print(f"{name}: {result}")