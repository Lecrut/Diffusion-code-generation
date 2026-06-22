def kelvin_to_celsius(temp_k):
    return temp_k - 273.15

def temperature_difference(kelvin1, kelvin2):
    return abs(kelvin1 - kelvin2)

if __name__ == '__main__':
    sample_temps = {
        'temp1': 300,
        'temp2': 298
    }
    diff_celsius = temperature_difference(sample_temps['temp1'], sample_temps['temp2'])
    print(f"Temperature Difference (Celsius): {diff_celsius}")