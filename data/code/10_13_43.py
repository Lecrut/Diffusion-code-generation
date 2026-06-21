def is_first_temp_greater(temp1, temp2):
    if not isinstance(temp1, int) or not isinstance(temp2, int):
        raise ValueError("Both temperatures must be integers.")
    return temp1 > temp2

if __name__ == '__main__':
    first_temperature = 50
    second_temperature = 45
    is_greater_result = is_first_temp_greater(first_temperature, second_temperature)
    print(is_greater_result)