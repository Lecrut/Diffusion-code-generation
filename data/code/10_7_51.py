def check_temperature_difference(temp1, temp2):
    return abs(temp1 - temp2) <= 1

if __name__ == '__main__':
    temperature1 = 15.0
    temperature2 = 16.3
    result = check_temperature_difference(temperature1, temperature2)
    print(result)