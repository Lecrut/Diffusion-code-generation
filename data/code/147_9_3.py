import functools
def sort_complex_numbers(complex_list):
    return sorted(complex_list, key=lambda c: (c.real, c.imag))
if __name__ == '__main__':
    sample_list = [1 + 2j, 3.5 + 1j, 1.5 + 4j, -0.5 + 0j, 3.5 + 0j, 1 + 1j]
    sorted_list = sort_complex_numbers(sample_list)
    print(sorted_list)