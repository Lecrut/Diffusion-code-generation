def is_negative(num):
    return num < 0

if __name__ == '__main__':
    test_values = [-5, 0, 3]
    results = {x: is_negative(x) for x in test_values}
    print(results)