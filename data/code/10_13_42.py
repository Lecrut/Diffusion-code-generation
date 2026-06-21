def is_first_temp_greater(temp1, temp2):
    INTEGER_TYPE = int
    if not isinstance(temp1, INTEGER_TYPE) or not isinstance(temp2, INTEGER_TYPE):
        raise ValueError("Both temperatures must be integers.")
    return temp1 > temp2

if __name__ == '__main__':
    SAMPLE_TEMP_ONE = 45
    SAMPLE_TEMP_TWO = 30
    RESULT = is_first_temp_greater(SAMPLE_TEMP_ONE, SAMPLE_TEMP_TWO)
    print(RESULT)