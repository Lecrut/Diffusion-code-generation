def compare_temperatures(temp1, temp2):
    difference = abs(temp1 - temp2)
    
    if temp1 > temp2:
        relative_magnitude = f"{temp1} is greater than {temp2}"
    elif temp1 < temp2:
        relative_magnitude = f"{temp1} is less than {temp2}"
    else:
        relative_magnitude = "Both temperatures are equal"
    
    return difference, relative_magnitude

if __name__ == '__main__':
    temp1 = 30
    temp2 = 25
    result = compare_temperatures(temp1, temp2)
    print(result)