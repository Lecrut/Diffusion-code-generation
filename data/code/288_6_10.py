def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9

def fahrenheit_to_kelvin(f):
    return (f + 459.67) * 5 / 9

def fahrenheit_to_reaumur(f):
    return (f - 32) * 4 / 9

def fahrenheit_to_rankine(f):
    return f + 459.67

if __name__ == '__main__':
    temp_f = 68
    print(f"Celsius: {fahrenheit_to_celsius(temp_f):.2f}")
    print(f"Kelvin: {fahrenheit_to_kelvin(temp_f):.2f}")
    print(f"Réaumur: {fahrenheit_to_reaumur(temp_f):.2f}")
    print(f"Rankine: {fahrenheit_to_rankine(temp_f):.2f}")