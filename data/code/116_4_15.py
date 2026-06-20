def sum_three(a, b, c):
    return a + b + c

if __name__ == '__main__':
    sample_values = {'x': 1, 'y': 2, 'z': 3}
    result = sum_three(**sample_values)
    print(result)