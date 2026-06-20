def multiply_complex_numbers(a, b):
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])

if __name__ == '__main__':
    result = multiply_complex_numbers((3, 2), (1, 7))
    print(result)