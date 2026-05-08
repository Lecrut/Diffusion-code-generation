import sys
def decision_simulator(value):
    if isinstance(value, int):
        if value > 0:
            return "Positive Action"
        elif value == 0:
            return "Neutral Action"
        else:
            return "Negative Action"
    elif isinstance(value, str):
        if value.lower() == "high":
            return "High Priority"
        elif value.lower() == "low":
            return "Low Priority"
        else:
            return "Unknown String Input"
    else:
        return "Invalid Data Type"
if __name__ == '__main__':
    test_inputs = [
        10,
        -5,
        0,
        500,
        "High",
        "low",
        "medium",
        3.14,
        None
    ]
    for input_value in test_inputs:
        result = decision_simulator(input_value)
        print(f"Input: {input_value} -> Result: {result}")
        print("-" * 20)