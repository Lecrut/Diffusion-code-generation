def complex_condition(a, b, c):
    return (a > 0) and (b < 10) and (c == 'test')

if __name__ == '__main__':
    result = complex_condition(5, 3, 'test')
    print(result)