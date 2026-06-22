def are_temperatures_close(temp1, temp2, tolerance=1):
    return abs(temp1 - temp2) <= tolerance

if __name__ == '__main__':
    temp_a = 23.5
    temp_b = 24.0
    print(are_temperatures_close(temp_a, temp_b))