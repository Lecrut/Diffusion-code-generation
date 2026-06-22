def calculate_temperature_difference(temp1, temp2):
    return abs(temp1 - temp2)

if __name__ == '__main__':
    SAMPLE_TEMP1 = 75.0
    SAMPLE_TEMP2 = 68.5
    result = calculate_temperature_difference(SAMPLE_TEMP1, SAMPLE_TEMP2)
    print(result)