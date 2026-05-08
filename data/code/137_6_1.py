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
    temperature1 = -5
    temperature2 = 15
    temperature3 = 35
    temperature4 = 0
    temperature5 = -15
    print(f"Temperature {temperature1}: {categorize_temperature(temperature1)}")
    print(f"Temperature {temperature2}: {categorize_temperature(temperature2)}")
    print(f"Temperature {temperature3}: {categorize_temperature(temperature3)}")
    print(f"Temperature {temperature4}: {categorize_temperature(temperature4)}")
    print(f"Temperature {temperature5}: {categorize_temperature(temperature5)}")