def check_temperature_difference(temp1, temp2, tolerance=1):
    return abs(temp1 - temp2) <= tolerance

if __name__ == '__main__':
    temperature1 = 20.3
    temperature2 = 20.8
    result = check_temperature_difference(temperature1, temperature2)
    print(result)