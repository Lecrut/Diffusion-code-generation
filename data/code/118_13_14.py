def multiply_complex_numbers(a, b):
    real_part = (a[0] * b[0]) - (a[1] * b[1])
    imag_part = (a[0] * b[1]) + (a[1] * b[0])
    return complex(real_part, imag_part)

if __name__ == '__main__':
    sample_a = (3, 2)
    sample_b = (1, -2)
    result = multiply_complex_numbers(sample_a, sample_b)
    print(result)