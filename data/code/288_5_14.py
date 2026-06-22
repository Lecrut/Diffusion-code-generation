def kelvin_to_celsius(temp_k):
    return temp_k - 273.15

def temperature_difference_kelvin(kelvin1, kelvin2):
    difference = abs(kelvin1 - kelvin2)
    celsius_diff = kelvin_to_celsius(difference)
    return celsius_diff

if __name__ == '__main__':
    sample_temp1 = 300
    sample_temp2 = 295
    result = temperature_difference_kelvin(sample_temp1, sample_temp2)
    print(f"Temperature Difference in Celsius: {result}")