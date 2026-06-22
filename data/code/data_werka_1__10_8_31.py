def are_temperatures_within_tolerance(temp1, temp2, tolerance=1):
    return abs(temp1 - temp2) <= tolerance

if __name__ == '__main__':
    temp_a = 75.3
    temp_b = 76.8
    result = are_temperatures_within_tolerance(temp_a, temp_b)
    print(result)