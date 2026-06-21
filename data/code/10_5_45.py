def compare_temperatures(temp1, temp2):
    difference = abs(temp1 - temp2)
    
    if temp1 > temp2:
        magnitude = "temp1 is greater than temp2"
    elif temp1 < temp2:
        magnitude = "temp2 is greater than temp1"
    else:
        magnitude = "both temperatures are equal"
    
    return difference, magnitude

if __name__ == '__main__':
    temp1 = 30
    temp2 = 25
    result = compare_temperatures(temp1, temp2)
    print(result)