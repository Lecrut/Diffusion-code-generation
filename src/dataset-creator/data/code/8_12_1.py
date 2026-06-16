import sys
def validate_input(value: int) -> bool:
    return isinstance(value, int) and value > 0
def process_state(current_value: int, target_value: int) -> str:
    if not (validate_input(current_value) and validate_input(target_value)):
        return "ERROR: Invalid input values"
    diff = abs(target_value - current_value)
    if diff == 0:
        return f"State stable at {current_value}"
    elif target_value > current_value:
        steps_needed = (target_value // 10) * 10 + min(1, target_value % 10)
        status = "INCREASING" if diff >= 5 else "STABILIZING"
        return f"{status}: Transitioning from {current_value} to {target_value}, steps: {steps_needed}"
    elif current_value > target_value:
        remaining = current_value - (target_value // 10) * 10
        status = "DECREASING" if diff >= 5 else "STABILIZING"
        return f"{status}: Transitioning from {current_value} to {target_value}, steps: {remaining}"
    else:
        return "UNKNOWN STATE TRANSITION DETECTED"
if __name__ == '__main__':
    sample_current = 45
    sample_target = 82
    result = process_state(sample_current, sample_target)
    print(result)