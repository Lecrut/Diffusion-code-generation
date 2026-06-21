def validate_temperatures(temp1, temp2):
    if not (isinstance(temp1, (int, float)) and isinstance(temp2, (int, float))):
        raise ValueError("Both temperatures must be numbers")

def calculate_mean(temp1, temp2):
    validate_temperatures(temp1, temp2)
    return round((temp1 + temp2) / 2, 2)

if __name__ == '__main__':
    sample_temp1 = 35.7
    sample_temp2 = 40.2
    try:
        mean_temperature = calculate_mean(sample_temp1, sample_temp2)
        print(mean_temperature)
    except ValueError as e:
        print(e)