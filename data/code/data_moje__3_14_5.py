def fahrenheit_to_kelvin(fahrenheit: float) -> float:
    return (fahrenheit - 32.0) * 5.0 / 9.0 + 273.15

def main() -> None:
    samples = [32.0, 212.0, 98.6, -40.0, 0.0]
    for f in samples:
        result = fahrenheit_to_kelvin(f)
        print(result)

if __name__ == '__main__':
    main()