from functools import reduce

def find_min_real_part(complex_list):
    return reduce(lambda x, y: x if x.real < y.real else y, complex_list)

if __name__ == '__main__':
    sample_complex = [3 + 4j, 1 + 1j, 2 + 2j, -1 - 1j]
    result = find_min_real_part(sample_complex)
    print(result)