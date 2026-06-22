from typing import List

def liters_to_milliliters(amount: float) -> float:
    return amount * 1000.0

if __name__ == "__main__":
    test_values: List[float] = [1.5, 0.001, 10.0, 42.9]
    for value in test_values:
        result = liters_to_milliliters(value)
        print(f"{value} liters is {result} milliliters")