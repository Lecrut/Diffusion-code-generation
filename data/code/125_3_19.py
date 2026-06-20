def arithmetic_operations(operations_dict):
    result_add = operations_dict['add'](15, 7)
    result_subtract = operations_dict['subtract'](15, 7)
    return result_add, result_subtract

if __name__ == '__main__':
    operations = {
        'add': lambda x, y: x + y,
        'subtract': lambda x, y: x - y
    }
    sum_result, difference_result = arithmetic_operations(operations)
    print(f"Sum: {sum_result}")
    print(f"Difference: {difference_result}")