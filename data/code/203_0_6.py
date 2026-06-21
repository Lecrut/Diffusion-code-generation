def compare_numbers(a, b):
    result = {
        1: 'Greater',
        -1: 'Lesser',
        0: 'Equal'
    }[cmp(a, b)]
    return result

if __name__ == '__main__':
    num1 = 5
    num2 = 3
    print(compare_numbers(num1, num2))