def is_first_temp_greater(temp1, temp2):
    if not isinstance(temp1, int) or not isinstance(temp2, int):
        raise ValueError("Both temperatures must be integers.")
    return temp1 > temp2

if __name__ == '__main__':
    SAMPLE_TEMP_1 = 45
    SAMPLE_TEMP_2 = 30
    result = is_first_temp_greater(SAMPLE_TEMP_1, SAMPLE_TEMP_2)
    print(result)