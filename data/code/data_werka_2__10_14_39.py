def compare_temperatures(temp1, temp2):
    return max(temp1, temp2)

if __name__ == '__main__':
    SAMPLE_TEMP_1 = 29.0
    SAMPLE_TEMP_2 = 31.5
    higher_temperature = compare_temperatures(SAMPLE_TEMP_1, SAMPLE_TEMP_2)
    print(higher_temperature)