def temperature_difference(temp1, temp2):
    difference = abs(temp1 - temp2)
    
    if temp1 > temp2:
        magnitude = "first temperature is higher"
    elif temp1 < temp2:
        magnitude = "second temperature is higher"
    else:
        magnitude = "both temperatures are equal"
    
    return difference, magnitude

if __name__ == '__main__':
    temp1 = 30
    temp2 = 25
    result = temperature_difference(temp1, temp2)
    print(result)