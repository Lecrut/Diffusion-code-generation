def calculate_temperature_difference(temp1, temp2):
    if not isinstance(temp1, (int, float)) or not isinstance(temp2, (int, float)):
        raise ValueError("Both temperatures must be numbers.")
    return abs(temp1 - temp2)

if __name__ == '__main__':
    sample_temp1 = 28.3
    sample_temp2 = 35.7
    try:
        result = calculate_temperature_difference(sample_temp1, sample_temp2)
        print(result)
    except ValueError as e:
        print(e)