def convert_temperature(fahrenheit):
    if not isinstance(fahrenheit, (int, float)):
        raise ValueError("Input must be a number.")
    
    celsius = (fahrenheit - 32) * 5/9
    kelvin = (fahrenheit - 32) * 5/9 + 273.15
    reaumur = (fahrenheit - 32) * 4/9
    rankine = fahrenheit + 459.67

    return {
        "Celsius": celsius,
        "Kelvin": kelvin,
        "Réaumur": reaumur,
        "Rankine": rankine
    }

if __name__ == '__main__':
    sample_fahrenheit = 77.0
    results = convert_temperature(sample_fahrenheit)
    print(f"Fahrenheit {sample_fahrenheit}°F is:")
    for scale, temp in results.items():
        print(f"{scale}: {temp:.2f}")