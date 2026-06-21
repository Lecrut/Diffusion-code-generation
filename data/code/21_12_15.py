def greatest_of_three(num1, num2, num3):
    values = {'a': num1, 'b': num2, 'c': num3}
    max_val = float('-inf')
    max_key = None
    for key in values:
        current = values[key]
        if max_key is None or current > max_val:
            max_val = current
            max_key = key
    return max_val

if __name__ == '__main__':
    val1 = -10
    val2 = -5
    val3 = -20
    result = greatest_of_three(val1, val2, val3)
    print(result)