def compare_temperatures(temp1, temp2):
    difference = abs(temp1 - temp2)
    if temp1 > temp2:
        return f"Temperature 1 is higher than Temperature 2 by {difference} degrees."
    elif temp1 < temp2:
        return f"Temperature 2 is higher than Temperature 1 by {difference} degrees."
    else:
        return "Both temperatures are equal."

if __name__ == '__main__':
    temp1 = 30.5
    temp2 = 25.0
    result = compare_temperatures(temp1, temp2)
    print(result)