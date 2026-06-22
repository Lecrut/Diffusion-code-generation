def calculate_ratio(numerator, denominator):
    if denominator == 0:
        return "Error: Division by zero"
    return numerator / denominator

if __name__ == '__main__':
    print("--- Scenario 1: Calculating Ratio ---")
    num_a = 20
    num_b = 4
    result = calculate_ratio(num_a, num_b)
    print(f"Ratio of {num_a}:{num_b} is {result}")