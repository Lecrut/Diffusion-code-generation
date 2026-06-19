def are_temperatures_within_tolerance(temp1, temp2, tolerance=1):
    return abs(temp1 - temp2) <= tolerance

if __name__ == '__main__':
    temp_a = 23.5
    temp_b = 24.0
    result = are_temperatures_within_tolerance(temp_a, temp_b)
    print(result)