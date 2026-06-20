def multiply_complex_numbers(a, b):
    real_part = a.real * b.real - a.imag * b.imag
    imag_part = a.real * b.imag + a.imag * b.real
    return complex(real_part, imag_part)

if __name__ == '__main__':
    result1 = multiply_complex_numbers(3+4j, 1-2j)
    print(result1)
    result2 = multiply_complex_numbers(2+3j, 4-5j)
    print(result2)