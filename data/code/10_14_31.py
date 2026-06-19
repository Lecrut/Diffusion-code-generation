def is_first_temp_greater(temp1, temp2):
    if not isinstance(temp1, int) or not isinstance(temp2, int):
        raise ValueError("Both temperature arguments must be integers.")
    return temp1 > temp2

if __name__ == '__main__':
    sample_temp1 = 30
    sample_temp2 = 25
    result = is_first_temp_greater(sample_temp1, sample_temp2)
    print(result)