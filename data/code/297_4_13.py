def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

if __name__ == '__main__':
    celsius_sample = 0.0
    fahrenheit_result = celsius_to_fahrenheit(celsius_sample)
    print(f"{celsius_sample}°C is {fahrenheit_result}°F")

    celsius_sample_2 = -40.0
    fahrenheit_result_2 = celsius_to_fahrenheit(celsius_sample_2)
    print(f"{celsius_sample_2}°C is {fahrenheit_result_2}°F")