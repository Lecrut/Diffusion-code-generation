def temperature_difference(temp1, temp2):
    difference = abs(temp1 - temp2)
    if temp1 > temp2:
        magnitude = f"{temp1} is greater than {temp2}"
    elif temp1 < temp2:
        magnitude = f"{temp1} is less than {temp2}"
    else:
        magnitude = "Both temperatures are equal"
    return difference, magnitude

if __name__ == '__main__':
    sample_temp1 = 25.0
    sample_temp2 = 30.0
    result = temperature_difference(sample_temp1, sample_temp2)
    print(f"Difference: {result[0]}, Magnitude: {result[1]}")