def multiply_complex_numbers(a, b):
    real_part = (a[0] * b[0]) - (a[1] * b[1])
    imag_part = (a[0] * b[1]) + (a[1] * b[0])
    return complex(real_part, imag_part)

if __name__ == '__main__':
    sample_a = 5 + 6j
    sample_b = 7 - 8j
    result = multiply_complex_numbers((sample_a.real, sample_a.imag), (sample_b.real, sample_b.imag))
    print(result)