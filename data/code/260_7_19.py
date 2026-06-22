def filter_complex_numbers(set1, set2):
    return {num for num in set1 | set2 if num.real > 0 and num.imag > 0}

if __name__ == '__main__':
    sample_set1 = {3+4j, -1-1j, 5+2j}
    sample_set2 = {-2+3j, 4-5j, 6+7j}
    result = filter_complex_numbers(sample_set1, sample_set2)
    print(result)