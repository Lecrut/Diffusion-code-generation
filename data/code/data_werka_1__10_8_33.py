def compare_temperatures(temp1, temp2, tolerance=1):
    return abs(temp1 - temp2) <= tolerance

if __name__ == '__main__':
    temperature1 = 75.5
    temperature2 = 76.0
    result = compare_temperatures(temperature1, temperature2)
    print(result)