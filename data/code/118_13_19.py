def multiply_complex(a, b):
    if not (isinstance(a, complex) and isinstance(b, complex)):
        raise ValueError("Both inputs must be complex numbers")
    
    real_part = a.real * b.real - a.imag * b.imag
    imag_part = a.real * b.imag + a.imag * b.real
    
    return complex(real_part, imag_part)

if __name__ == '__main__':
    try:
        result = multiply_complex(3+4j, 1-2j)
        print(result)
    except ValueError as e:
        print(e)