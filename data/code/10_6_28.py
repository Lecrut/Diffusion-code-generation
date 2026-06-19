def temperature_difference(temp1, temp2):
    difference = abs(temp1 - temp2)
    if temp1 > temp2:
        magnitude = f"{temp1} is greater than {temp2} by {difference}"
    elif temp1 < temp2:
        magnitude = f"{temp2} is greater than {temp1} by {difference}"
    else:
        magnitude = "Both temperatures are equal"
    return difference, magnitude

if __name__ == '__main__':
    temp_a = 30.5
    temp_b = 22.8
    diff, mag = temperature_difference(temp_a, temp_b)
    print(f"Difference: {diff}, Magnitude: {mag}")