def print_complex_list(complex_numbers):
    for num in complex_numbers:
        print(f"{num.real} + {num.imag}j")

if __name__ == '__main__':
    sample_list = [2+3j, 4-5j, -1+0j]
    print_complex_list(sample_list)