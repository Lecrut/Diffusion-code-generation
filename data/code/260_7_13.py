def filter_complex_numbers(set1, set2):
    result = set()
    for num in set1:
        if num.real > 0 and num.imag > 0:
            result.add(num)
    for num in set2:
        if num.real > 0 and num.imag > 0:
            result.add(num)
    return result

if __name__ == '__main__':
    sample_set1 = {3 + 4j, -1 - 1j, 5 + 2j, 0 + 7j}
    sample_set2 = {-2 - 3j, 6 + 8j, 1 + 1j, 0 + 0j}
    filtered_result = filter_complex_numbers(sample_set1, sample_set2)
    print(filtered_result)