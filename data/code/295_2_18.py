def fahrenheit_to_celsius(fahrenheit):
    try:
        celsius = (fahrenheit - 32) * 5 / 9
        return int(celsius)
    except TypeError:
        raise ValueError("Input must be a number")

if __name__ == '__main__':
    sample_values = [32, 212, 0, 100]
    for temp in sample_values:
        print(f"{temp}F is {fahrenheit_to_celsius(temp)}C")