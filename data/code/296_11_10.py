def calculate_ratio(numerator, denominator):
    if denominator == 0:
        return 'undefined'
    ratio = numerator / denominator
    return f'{numerator}:{denominator}'
if __name__ == '__main__':
    result = calculate_ratio(10, 2)
    print(result)
    result = calculate_ratio(5, 0)
    print(result)