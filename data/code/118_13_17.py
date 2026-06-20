def multiply_complex(a, b):
    real = a.real * b.real - a.imag * b.imag
    imag = a.real * b.imag + a.imag * b.real
    return complex(real, imag)

if __name__ == '__main__':
    c1 = complex(3, 2)
    c2 = complex(1, 7)
    result = multiply_complex(c1, c2)
    print(result)