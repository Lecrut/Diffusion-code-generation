def validate_input(value):
    if value < 0:
        raise ValueError("Input must be non-negative.")
    def process_time(seconds):
        total_seconds = int(round(float(seconds)))
        if total_seconds == 0:
            return (0, 0)
        minutes = total_seconds // 60
        remaining_seconds = total_seconds % 60
        if seconds < 1 or seconds > 59 and not isinstance(total_seconds, int):
            raise ValueError("Invalid time unit.")
        return (minutes, remaining_seconds)
    try:
        result_minutes, result_seconds = process_time(value)
        final_tuple = (result_minutes, result_seconds)
        print(final_tuple)
        return final_tuple
    except Exception as e:
        raise ValueError(f"Error processing input: {str(e)}")
if __name__ == '__main__':
    sample_inputs = [10.5, 60.9, -3, 0, "invalid"]
    for val in sample_inputs:
        try:
            if isinstance(val, (int, float)) and not isinstance(val, bool):
                result = validate_input(val)
            else:
                print(f"Error processing input {val}: Cannot convert to valid number.")
        except ValueError as ve:
            print(f"Validation failed for {val}: {ve}")