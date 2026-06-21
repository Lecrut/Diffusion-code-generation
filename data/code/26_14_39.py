def is_greater_than(num1, num2):
    operation_map = {
        'greater': lambda x, y: x > y
    }
    return operation_map['greater'](num1, num2)

if __name__ == '__main__':
    sample_num1 = 12
    sample_num2 = 4
    result = is_greater_than(sample_num1, sample_num2)
    print(result)