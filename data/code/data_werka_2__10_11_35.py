def calculate_temperature_difference(temp1, temp2):
    return abs(temp1 - temp2)

if __name__ == '__main__':
    sample_temperatures = {
        'temp1': 45.0,
        'temp2': 60.3
    }
    
    result = calculate_temperature_difference(sample_temperatures['temp1'], sample_temperatures['temp2'])
    print(result)