def count_matching_values(array1, array2):
    return sum((1 for a, b in zip(array1, array2) if a == b))
if __name__ == '__main__':
    sample_array1 = [1, 2, 3, 2, 5, 5, 4, 1]
    sample_array2 = [1, 2, 3, 2, 6, 5, 4, 1]
    result = count_matching_values(sample_array1, sample_array2)
    print(result)