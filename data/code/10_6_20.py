def temperature_difference(temp1, temp2):
    difference = abs(temp1 - temp2)
    if temp1 > temp2:
        return f"The first temperature is higher by {difference} degrees."
    elif temp1 < temp2:
        return f"The second temperature is higher by {difference} degrees."
    else:
        return "Both temperatures are equal."

if __name__ == '__main__':
    temp1 = 30
    temp2 = 25
    result = temperature_difference(temp1, temp2)
    print(result)