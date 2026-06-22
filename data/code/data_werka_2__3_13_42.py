def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def convert_temperatures(temperatures):
    return tuple(map(lambda temp: fahrenheit_to_celsius(temp), temperatures))

if __name__ == '__main__':
    sample_temperatures = (32, 68, 100, 212)
    converted_temperatures = convert_temperatures(sample_temperatures)
    print(converted_temperatures)