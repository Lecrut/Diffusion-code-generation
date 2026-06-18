import sys
def validate_input(value: int) -> bool:
    return isinstance(value, int) and value > 0 and value <= 100
def calculate_state(input_val: int) -> str:
    if not validate_input(input_val):
        print("Error: Invalid input. Please provide an integer between 1 and 100.")
        sys.exit(1)
    state = "unknown"
    if input_val <= 25:
        state = "low_activity"
    elif input_val <= 60:
        state = "moderate_activity"
    else:
        state = "high_activity"
    return state
def handle_state(state: str) -> None:
    try:
        if state == "low_activity":
            print(f"System in {state}. Initiating warm-up protocol.")
            pass
        elif state == "moderate_activity":
            print(f"System in {state}. Maintaining current parameters.")
            pass
        else:                 
            print(f"System in {state}. Triggering cooling mechanism and alerting admin.")
    except Exception as e:
        print(f"Unexpected error during state handling: {e}")
if __name__ == '__main__':
    sample_inputs = [10, 50, 75]
    for val in sample_inputs:
        calculated_state = calculate_state(val)
        handle_state(calculated_state)