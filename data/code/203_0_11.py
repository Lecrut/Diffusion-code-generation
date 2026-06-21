def compare_values(a, b):
    comparisons = {
        1: 'Greater',
        -1: 'Lesser',
        0: 'Equal'
    }
    return comparisons[a - b]

if __name__ == '__main__':
    num1 = 5
    num2 = 3
    result = compare_values(num1, num2)
    print(result)