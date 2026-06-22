def fahrenheit_to_kelvin(fahrenheit: float) -> float:
    return (fahrenheit - 32.0) * 5.0 / 9.0 + 273.15

def main() -> None:
    sample_values = [32.0, 212.0, 0.0, -40.0]
    results = [fahrenheit_to_kelvin(val) for val in sample_values]
    for f_val, k_val in zip(sample_values, results):
        print(f"{f_val} F = {k_val} K")

if __name__ == "__main__":
    main()