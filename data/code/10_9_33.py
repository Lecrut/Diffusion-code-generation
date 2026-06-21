def compare_temperatures(temp1, temp2):
    if temp1 > temp2:
        return "First temperature is higher."
    elif temp1 < temp2:
        return "Second temperature is higher."
    else:
        return "Both temperatures are equal."

if __name__ == '__main__':
    temp1 = 23.5
    temp2 = 25.0
    result = compare_temperatures(temp1, temp2)
    print(result)