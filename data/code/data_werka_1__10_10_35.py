def compare_temperatures(temp1, temp2):
    if temp1 > temp2:
        return "First temperature is higher."
    elif temp1 < temp2:
        return "Second temperature is higher."
    else:
        return "Both temperatures are equal."

if __name__ == '__main__':
    sample_temp1 = 23.5
    sample_temp2 = 23.5
    result = compare_temperatures(sample_temp1, sample_temp2)
    print(result)