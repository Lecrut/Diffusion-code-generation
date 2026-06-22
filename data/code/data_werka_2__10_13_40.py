def is_first_temp_greater(temp1, temp2):
    if not isinstance(temp1, int) or not isinstance(temp2, int):
        raise ValueError("Both temperatures must be integers.")
    return temp1 > temp2

if __name__ == '__main__':
    sample_temp_a = 35
    sample_temp_b = 40
    result_comparison = is_first_temp_greater(sample_temp_a, sample_temp_b)
    print(result_comparison)