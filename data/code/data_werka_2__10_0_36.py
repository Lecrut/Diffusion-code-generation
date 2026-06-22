def compare_temperatures(temp1, temp2):
    if temp1 > temp2:
        return (temp1, 'higher')
    elif temp1 < temp2:
        return (temp2, 'lower')
    else:
        return ('equal',)

if __name__ == '__main__':
    SAMPLE_TEMP_1 = 35.0
    SAMPLE_TEMP_2 = 40.0
    result = compare_temperatures(SAMPLE_TEMP_1, SAMPLE_TEMP_2)
    print(result)

    ANOTHER_SAMPLE_TEMP_1 = 42.5
    ANOTHER_SAMPLE_TEMP_2 = 42.5
    another_result = compare_temperatures(ANOTHER_SAMPLE_TEMP_1, ANOTHER_SAMPLE_TEMP_2)
    print(another_result)