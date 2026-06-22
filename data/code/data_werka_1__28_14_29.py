def compare_values(a: float, b: float) -> bool:
    return a > b

if __name__ == '__main__':
    value1 = 3.14159
    value2 = 2.71828
    result = compare_values(value1, value2)
    print(result)