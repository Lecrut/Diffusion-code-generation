C_TO_F = 9 / 5
F_TO_C = 5 / 9
K_TO_C = -273.15

def celsius_to_fahrenheit(celsius):
    return (celsius * C_TO_F) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * F_TO_C

def kelvin_to_celsius(kelvin):
    return kelvin + K_TO_C

def average_temperature(temp1, scale1, temp2, scale2, temp3, scale3):
    temp1_c = temp1 if scale1 == 'C' else celsius_to_fahrenheit(temp1) if scale1 == 'F' else kelvin_to_celsius(temp1)
    temp2_c = temp2 if scale2 == 'C' else celsius_to_fahrenheit(temp2) if scale2 == 'F' else kelvin_to_celsius(temp2)
    temp3_c = temp3 if scale3 == 'C' else celsius_to_fahrenheit(temp3) if scale3 == 'F' else kelvin_to_celsius(temp3)
    return (temp1_c + temp2_c + temp3_c) / 3

if __name__ == '__main__':
    avg_temp = average_temperature(25, 'C', 68, 'F', 300, 'K')
    print(f"The average temperature is {avg_temp:.2f}°C")