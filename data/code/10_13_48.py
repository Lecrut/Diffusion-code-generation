def validate_temperature(temp):
    if not isinstance(temp, int):
        raise ValueError("Temperature must be an integer.")

def is_first_temp_greater(temp1, temp2):
    validate_temperature(temp1)
    validate_temperature(temp2)
    return temp1 > temp2

if __name__ == '__main__':
    try:
        sample_temp_first = 50
        sample_temp_second = 45
        result = is_first_temp_greater(sample_temp_first, sample_temp_second)
        print(result)
    except ValueError as e:
        print(e)