def is_first_temp_greater(temp1, temp2):
    if not isinstance(temp1, int) or not isinstance(temp2, int):
        raise ValueError("Both temperature arguments must be integers.")
    return temp1 > temp2

if __name__ == '__main__':
    temp_a = 30
    temp_b = 25
    result = is_first_temp_greater(temp_a, temp_b)
    print(result)