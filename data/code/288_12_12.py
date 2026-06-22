def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def average_temperature(celsius, fahrenheit, kelvin):
    celsius_sum = celsius + fahrenheit_to_celsius(fahrenheit) + kelvin_to_celsius(kelvin)
    return celsius_sum / 3

if __name__ == '__main__':
    sample_celsius = 25.0
    sample_fahrenheit = 68.0
    sample_kelvin = 300.15
    avg_temp = average_temperature(sample_celsius, sample_fahrenheit, sample_kelvin)
    print(f"The average temperature is {avg_temp:.2f}°C")