def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def average_temperature(temp1, scale1, temp2, scale2, temp3, scale3):
    if scale1 not in ['C', 'F', 'K'] or scale2 not in ['C', 'F', 'K'] or scale3 not in ['C', 'F', 'K']:
        raise ValueError("Invalid temperature scale")
    
    temp1_c = celsius_to_fahrenheit(temp1) if scale1 == 'F' else kelvin_to_celsius(temp1) if scale1 == 'K' else temp1
    temp2_c = celsius_to_fahrenheit(temp2) if scale2 == 'F' else kelvin_to_celsius(temp2) if scale2 == 'K' else temp2
    temp3_c = celsius_to_fahrenheit(temp3) if scale3 == 'F' else kelvin_to_celsius(temp3) if scale3 == 'K' else temp3
    
    return (temp1_c + temp2_c + temp3_c) / 3

if __name__ == '__main__':
    avg_temp = average_temperature(25, 'C', 68, 'F', 300, 'K')
    print(f"The average temperature is {avg_temp}°C")