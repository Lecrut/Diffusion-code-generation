def calculate_mean(temperature_data):
    temp1 = temperature_data.get('temp1')
    temp2 = temperature_data.get('temp2')
    
    if not (isinstance(temp1, (int, float)) and isinstance(temp2, (int, float))):
        raise ValueError("Both temperatures must be numbers")
    
    return round((temp1 + temp2) / 2, 2)

if __name__ == '__main__':
    sample_temperatures = {
        'temp1': 35.2,
        'temp2': 40.7
    }
    try:
        mean_temperature = calculate_mean(sample_temperatures)
        print(mean_temperature)
    except ValueError as e:
        print(e)