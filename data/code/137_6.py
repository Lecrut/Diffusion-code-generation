def categorize_temperature(temp):
    if temp <= 0:
        if temp < -10:
            return 'Freezing'
        else:
            return 'Freezing'
    elif temp <= 25:
        return 'Moderate'
    else:
        return 'Hot'
if __name__ == '__main__':
    temp1 = -5
    temp2 = 15
    temp3 = 35
    temp4 = 0
    temp5 = -15
    print(f"Temperature {temp1}: {categorize_temperature(temp1)}")
    print(f"Temperature {temp2}: {categorize_temperature(temp2)}")
    print(f"Temperature {temp3}: {categorize_temperature(temp3)}")
    print(f"Temperature {temp4}: {categorize_temperature(temp4)}")
    print(f"Temperature {temp5}: {categorize_temperature(temp5)}")