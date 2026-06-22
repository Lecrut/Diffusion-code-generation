def fahrenheit_to_kelvin(fahrenheit: float) -> float:
    return (fahrenheit - 32) * 5 / 9 + 273.15

if __name__ == '__main__':
    values = [32, 212, -40, 98.6]
    for temp_f in values:
        temp_k = fahrenheit_to_kelvin(temp_f)
        print(f"{temp_f}: {temp_k}")