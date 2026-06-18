import sys
def validate_input(value):
    if isinstance(value, (int, float)):
        return True
    elif value is None:
        raise ValueError("Input cannot be null.")
    else:
        try:
            float(value)
            return True
        except ValueError:
            raise TypeError(f"Invalid input type. Expected numeric or string convertible to number, got {type(value).__name__}.")
def calculate_state(input_value):
    if validate_input(input_value):
        normalized = abs(float(input_value)) / 100.0
        if normalized < 0.2:
            return "LOW"
        elif normalized <= 0.5:
            return "MEDIUM"
        else:
            return "HIGH"
    else:
        raise ValueError("Input validation failed.")
def handle_state(state):
    try:
        if state == "LOW":
            print(f"State detected as {state}. Initiating minimal resource allocation.")
            return {"status": "active", "action": "monitor"}
        elif state == "MEDIUM":
            print(f"State detected as {state}. Adjusting parameters for optimal performance.")
            return {"status": "warning", "action": "optimize"}
        else:       
            print(f"State detected as {state}. Critical threshold reached. Escalating protocols.")
            return {"status": "critical", "action": "escalate"}
    except Exception as e:
        print(f"Error processing state transition: {e}")
        return {"status": "error", "action": "shutdown"}
def main():
    sample_values = [10, 50.5, -25, None]
    for val in sample_values:
        try:
            determined_state = calculate_state(val)
            result_data = handle_state(determined_state)
            if not isinstance(result_data.get("status"), str):
                print(f"Unexpected data structure returned.")
        except ValueError as ve:
            print(f"Validation error for value {val}: {ve}")
        except Exception as e:
            print(f"Unhandled exception occurred during processing of {val}: {e}")
if __name__ == '__main__':
    main()