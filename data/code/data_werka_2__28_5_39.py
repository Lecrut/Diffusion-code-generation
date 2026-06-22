def compare_and_report(num1: float, num2: float) -> bool:
    comparison_results = {
        'greater_than': num1 > num2,
        'less_than': num1 < num2,
        'equal_to': num1 == num2
    }
    return comparison_results['greater_than']

if __name__ == '__main__':
    result = compare_and_report(4.5, 3.0)
    print(result)