def compare_and_report(num1: float, num2: float) -> bool:
    comparison_map = {
        'greater_than': lambda x, y: x > y,
        'less_than': lambda x, y: x < y,
        'equal_to': lambda x, y: x == y
    }
    return comparison_map['greater_than'](num1, num2)

if __name__ == '__main__':
    sample_values = [
        (3.5, 2.0),
        (4.5, 3.0),
        (5.0, 2.8),
        (6.0, 4.5)
    ]
    
    for num1, num2 in sample_values:
        result = compare_and_report(num1, num2)
        print(f"Is {num1} strictly greater than {num2}? {result}")