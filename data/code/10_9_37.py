def compare_temperatures(temp1, temp2):
    if temp1 > temp2:
        return "First temperature is higher."
    if temp1 < temp2:
        return "Second temperature is higher."
    return "Both temperatures are equal."

if __name__ == '__main__':
    temp_a = 30.0
    temp_b = 28.5
    result = compare_temperatures(temp_a, temp_b)
    print(result)