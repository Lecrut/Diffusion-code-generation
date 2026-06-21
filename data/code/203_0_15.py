def compare_numbers(a, b):
    comparisons = {
        1: 'Greater',
        -1: 'Lesser',
        0: 'Equal'
    }
    result = (a > b) - (a < b)
    return comparisons[result]

if __name__ == '__main__':
    num1 = 42
    num2 = 37
    result = compare_numbers(num1, num2)
    print(result)