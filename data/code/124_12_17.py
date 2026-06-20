def calculate_operations():
    a = 10
    b = 5

    addition = a + b
    subtraction = a - b
    multiplication = a * b
    division = a / b
    modulus = a % b
    exponentiation = a ** b

    return {
        "addition": addition,
        "subtraction": subtraction,
        "multiplication": multiplication,
        "division": division,
        "modulus": modulus,
        "exponentiation": exponentiation
    }

if __name__ == '__main__':
    results = calculate_operations()
    print(results)