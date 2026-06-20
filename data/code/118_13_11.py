def validate_complex_number(number):
    if not isinstance(number, complex) or number.imag == 0:
        raise ValueError("Input must be a non-zero imaginary complex number")

def multiply_complex(a, b):
    validate_complex_number(a)
    validate_complex_number(b)
    
    real_part = a.real * b.real - a.imag * b.imag
    imag_part = a.real * b.imag + a.imag * b.real
    return complex(real_part, imag_part)

if __name__ == '__main__':
    sample_a = 3 + 4j
    sample_b = 1 - 2j
    result = multiply_complex(sample_a, sample_b)
    print(result)