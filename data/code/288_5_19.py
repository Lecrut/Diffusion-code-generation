def kelvin_to_celsius(temp_k):
    return temp_k - 273.15

def temperature_difference_kelvin_to_celsius(kelvin1, kelvin2):
    celsius1 = kelvin_to_celsius(kelvin1)
    celsius2 = kelvin_to_celsius(kelvin2)
    return abs(celsius1 - celsius2)

if __name__ == '__main__':
    sample_values = {
        'temp1': 300,
        'temp2': 280
    }
    
    difference = temperature_difference_kelvin_to_celsius(sample_values['temp1'], sample_values['temp2'])
    print(f"Temperature Difference (Celsius): {difference}")