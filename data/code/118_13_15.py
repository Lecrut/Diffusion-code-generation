def multiply_complex(a, b):
    real_part = a.real * b.real - a.imag * b.imag
    imag_part = a.real * b.imag + a.imag * b.real
    return complex(real_part, imag_part)

if __name__ == '__main__':
    c1 = complex(3, 2)
    c2 = complex(1, 7)
    result = multiply_complex(c1, c2)
    print(result)