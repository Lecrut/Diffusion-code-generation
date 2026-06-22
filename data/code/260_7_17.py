def filter_complex_numbers(set1, set2):
    result = {num for num in set1 if num.real > 0 and num.imag > 0} & \
             {num for num in set2 if num.real > 0 and num.imag > 0}
    return result

if __name__ == '__main__':
    sample_set1 = {3 + 4j, -1 + 2j, 5 + 6j, 7 - 8j}
    sample_set2 = {2 + 3j, 4 - 5j, 6 + 7j, 8 + 9j}
    filtered_result = filter_complex_numbers(sample_set1, sample_set2)
    print(filtered_result)