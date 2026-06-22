def compare_temperatures(temp1, temp2):
    if temp1 > temp2:
        return "First temperature is higher."
    elif temp1 < temp2:
        return "Second temperature is higher."
    else:
        return "Both temperatures are equal."

if __name__ == '__main__':
    SAMPLE_TEMP1 = 30.0
    SAMPLE_TEMP2 = 28.5
    result = compare_temperatures(SAMPLE_TEMP1, SAMPLE_TEMP2)
    print(result)