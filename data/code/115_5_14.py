NUMERATOR = [10, 15, 7]
DENOMINATOR = [2, 3, 0]

def divide_elements(numerator_list, denominator_list):
    return [num / denom for num, denom in zip(numerator_list, denominator_list)]

if __name__ == '__main__':
    result = divide_elements(NUMERATOR, DENOMINATOR)
    print(result)