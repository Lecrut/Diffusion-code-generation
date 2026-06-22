def are_temperatures_within_tolerance(temp1, temp2, tolerance=1):
    return abs(temp1 - temp2) <= tolerance

if __name__ == '__main__':
    temp1 = 75.5
    temp2 = 76.0
    result = are_temperatures_within_tolerance(temp1, temp2)
    print(result)