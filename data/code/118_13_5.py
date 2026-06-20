def multiply_complex(a, b):
    if not (isinstance(a, complex) and isinstance(b, complex)):
        raise ValueError("Both arguments must be complex numbers.")
    
    real_part = a.real * b.real - a.imag * b.imag
    imag_part = a.real * b.imag + a.imag * b.real
    
    return complex(real_part, imag_part)

if __name__ == '__main__':
    sample_a = 3 + 4j
    sample_b = 1 - 2j
    result = multiply_complex(sample_a, sample_b)
    print(result)