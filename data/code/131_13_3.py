import sys
def decision_simulator(value):
    if isinstance(value, int):
        if value > 0:
            return "Positive Result"
        elif value == 0:
            return "Zero Value"
        else:
            return "Negative Value"
    elif isinstance(value, str):
        if value.lower() == "high":
            return "High Priority Action"
        elif value.lower() == "low":
            return "Low Priority Action"
        else:
            return "Unknown String Input"
    else:
        return "Invalid Data Type"
if __name__ == '__main__':
    sample_inputs = [
        10,
        -5,
        0,
        "High",
        "low",
        "medium",
        3.14,
        [1, 2, 3]
    ]
    print("--- Decision Simulation Results ---")
    for input_val in sample_inputs:
        result = decision_simulator(input_val)
        print(f"Input: {repr(input_val)} -> Result: {result}")
    print("---------------------------------")