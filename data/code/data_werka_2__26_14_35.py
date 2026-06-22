def compare_numbers(num1, num2):
    comparison_map = {
        'greater': num1 > num2,
        'less': num1 < num2,
        'equal': num1 == num2
    }
    return comparison_map['greater']

if __name__ == '__main__':
    sample_num1 = 7
    sample_num2 = 3
    result = compare_numbers(sample_num1, sample_num2)
    print(result)