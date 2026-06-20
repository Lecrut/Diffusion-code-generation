def multiply_complex_numbers(a, b):
    real_part = a.real * b.real - a.imag * b.imag
    imag_part = a.real * b.imag + a.imag * b.real
    return complex(real_part, imag_part)

if __name__ == '__main__':
    result = multiply_complex_numbers(complex(1, 2), complex(3, 4))
    print(result)