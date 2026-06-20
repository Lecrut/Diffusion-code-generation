def fahrenheit_to_kelvin(fahrenheit: float) -> float:
    return (fahrenheit + 459.67) * 5 / 9

def main() -> None:
    sample_fahrenheit_values = [-459.67, -40.0, 32.0, 98.6, 212.0, 1000.0]
    for f in sample_fahrenheit_values:
        k = fahrenheit_to_kelvin(f)
        print(f'Fahrenheit {f} = Kelvin {k}')
if __name__ == '__main__':
    main()