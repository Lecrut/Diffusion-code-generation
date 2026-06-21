def temperature_difference(temp1, temp2):
    difference = abs(temp1 - temp2)
    
    if temp1 > temp2:
        relative_magnitude = f"{temp1} is greater than {temp2} by {difference}"
    elif temp1 < temp2:
        relative_magnitude = f"{temp2} is greater than {temp1} by {difference}"
    else:
        relative_magnitude = "Both temperatures are equal"
    
    return difference, relative_magnitude

if __name__ == '__main__':
    temp1 = 30
    temp2 = 20
    diff, rel_mag = temperature_difference(temp1, temp2)
    print(f"Difference: {diff}")
    print(rel_mag)