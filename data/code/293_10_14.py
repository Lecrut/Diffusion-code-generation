def validate_temperature(value):
    if not isinstance(value, (int, float)):
        raise ValueError("Invalid temperature value")
    return value

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

if __name__ == '__main__':
    sample_celsius = 100
    sample_fahrenheit = 212

    validated_celsius = validate_temperature(sample_celsius)
    validated_fahrenheit = validate_temperature(sample_fahrenheit)

    print(f"{sample_celsius}C is {celsius_to_fahrenheit(validated_celsius):.2f}F")
    print(f"{sample_fahrenheit}F is {fahrenheit_to_celsius(validated_fahrenheit):.2f}C")