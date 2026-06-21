def validate_temperature(temp):
    if not isinstance(temp, (int, float)):
        raise ValueError("Temperature must be a number")

def calculate_mean(temp1, temp2):
    validate_temperature(temp1)
    validate_temperature(temp2)
    return round((temp1 + temp2) / 2, 2)

if __name__ == '__main__':
    sample_temp1 = 35.7
    sample_temp2 = 40.2
    try:
        mean_temperature = calculate_mean(sample_temp1, sample_temp2)
        print(mean_temperature)
    except ValueError as e:
        print(e)