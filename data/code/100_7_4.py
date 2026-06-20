def check_complex_condition(a, b, c):
    return (a > 0) and (b < 10) or (c == 'test')

if __name__ == '__main__':
    result = check_complex_condition(5, 3, 'test')
    print(result)