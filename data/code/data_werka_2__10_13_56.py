def is_first_temp_greater(temp1, temp2):
    if not isinstance(temp1, int) or not isinstance(temp2, int):
        raise ValueError("Both temperatures must be integers.")
    return temp1 > temp2

if __name__ == '__main__':
    temperature_one = 50
    temperature_two = 45
    is_greater = is_first_temp_greater(temperature_one, temperature_two)
    print(is_greater)