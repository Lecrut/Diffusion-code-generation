def are_temperatures_within_tolerance(temp1, temp2, tolerance=1):
    return abs(temp1 - temp2) <= tolerance

if __name__ == '__main__':
    sample_temp1 = 23.5
    sample_temp2 = 24.0
    result = are_temperatures_within_tolerance(sample_temp1, sample_temp2)
    print(result)