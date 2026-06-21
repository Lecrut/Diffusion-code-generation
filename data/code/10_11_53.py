def compute_temperature_difference(temp_data):
    temp1 = temp_data['temperature1']
    temp2 = temp_data['temperature2']
    return abs(temp1 - temp2)

if __name__ == '__main__':
    sample_temperatures = {
        'temperature1': 30.5,
        'temperature2': 25.8
    }
    result = compute_temperature_difference(sample_temperatures)
    print(result)