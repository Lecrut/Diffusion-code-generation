def logical_operations(x: bool, y: bool) -> tuple:
    and_result = x and y
    or_result = x or y
    return (and_result, or_result)

if __name__ == '__main__':
    sample_x = True
    sample_y = False
    result_and, result_or = logical_operations(sample_x, sample_y)
    print(f'AND Result: {result_and}')
    print(f'OR Result: {result_or}')