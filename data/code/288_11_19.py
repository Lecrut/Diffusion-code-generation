def kelvin_to_celsius(kelvin):
    if not isinstance(kelvin, (int, float)) or kelvin < 0:
        raise ValueError("Temperature in Kelvin must be a non-negative number")
    return kelvin - 273.15

def calculate_temperature_difference(temp1_kelvin, temp2_kelvin):
    return abs(kelvin_to_celsius(temp1_kelvin) - kelvin_to_celsius(temp2_kelvin))

if __name__ == '__main__':
    temp1 = 300
    temp2 = 290
    difference = calculate_temperature_difference(temp1, temp2)
    print(difference)