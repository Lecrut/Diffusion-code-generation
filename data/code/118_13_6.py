def multiply_complex(a, b):
    real_part = (a.real * b.real) - (a.imag * b.imag)
    imag_part = (a.real * b.imag) + (a.imag * b.real)
    return complex(real_part, imag_part)

if __name__ == '__main__':
    sample_a = 5 + 6j
    sample_b = -1 + 2j
    result = multiply_complex(sample_a, sample_b)
    print(result)