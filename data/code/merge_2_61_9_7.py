import math
def convert_seconds_to_hm(seconds: float) -> tuple[int, int]:
    if not isinstance(seconds, (int, float)):
        raise TypeError("Input must be an integer or a float.")
    if seconds < 0:
        raise ValueError("Seconds cannot be negative.")
    total_minutes = math.floor(seconds / 60)
    hours = int(total_minutes // 60)
    minutes = int(total_minutes % 60)
    return (hours, minutes)
if __name__ == '__main__':
    sample_seconds = 3725
    try:
        h, m = convert_seconds_to_hm(sample_seconds)
        print(f"{h} hours and {m} minutes")
        invalid_inputs = [None, "10", True]
        for test_val in invalid_inputs:
            try:
                result = convert_seconds_to_hm(test_val)
                if isinstance(result, tuple):
                    print(f"Unexpected success with {test_val}: {result}")
                else:
                    raise AssertionError("Function should not return anything other than a tuple.")
            except (TypeError, ValueError) as e:
                print(f"Caught expected error for input {type(test_val).__name__}: {e.__class__.__name__}")
    except Exception as general_error:
        print(f"Unexpected runtime error: {general_error}")