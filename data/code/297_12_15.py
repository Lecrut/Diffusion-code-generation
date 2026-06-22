def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

if __name__ == '__main__':
    sample_fahrenheit = -40
    sample_celsius = 0

    print(f"{sample_fahrenheit} F is {fahrenheit_to_celsius(sample_fahrenheit)} C")
    print(f"{sample_celsius} C is {celsius_to_fahrenheit(sample_celsius)} F")