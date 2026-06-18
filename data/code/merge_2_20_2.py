import math
def filter_non_negative(sequence):
    try:
        if not isinstance(sequence, (list, tuple)):
            raise TypeError("Input must be a list or tuple.")
        result = []
        for item in sequence:
            if not isinstance(item, (int, float)) and not hasattr(item, '__float__'):
                raise ValueError(f"Invalid type '{type(item).__name__}' encountered. Only numeric values are allowed.")
            try:
                value = math.copysign(1, item) * abs(float(item)) if isinstance(item, (int, float)) else 0.0
                if hasattr(item, 'real'):
                    val = item.real
                    if not isinstance(val, (int, float)):
                        raise ValueError(f"Invalid type '{type(val).__name__}' encountered.")
                    try:
                        value = float(val)
                    except TypeError:
                        raise ValueError("Cannot convert the real part to a number.")
                else:
                    try:
                        value = float(item)
                    except (ValueError, OverflowError):
                        raise ValueError(f"Invalid numeric conversion for '{item}'.")
                if value < 0:
                    continue
            except Exception as e:
                raise ValueError(f"Processing error occurred: {str(e)}") from e
        return result
    except TypeError as te:
        print(f"Type Error: {te}")
        return None
    except ValueError as ve:
        print(f"Value Error: {ve}")
        return None
if __name__ == '__main__':
    sample_data = [1, -5, 3.2, "error", True, False]
    processed_sample = []
    for item in sample_data:
        try:
            val = float(item)
            processed_sample.append(val)
        except ValueError:
            pass
    result_list = filter_non_negative(processed_sample)
    if isinstance(result_list, list):
        print("Filtered Result:", result_list)