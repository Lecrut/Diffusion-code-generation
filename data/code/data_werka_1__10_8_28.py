def are_temperatures_within_tolerance(temp1, temp2, tolerance=1):
    return abs(temp1 - temp2) <= tolerance

if __name__ == '__main__':
    temperature1 = 25.3
    temperature2 = 26.7
    result = are_temperatures_within_tolerance(temperature1, temperature2)
    print(result)