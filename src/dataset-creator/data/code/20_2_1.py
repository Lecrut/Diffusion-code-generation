import math
def filter_non_negative(sequence):
    try:
        if not isinstance(sequence, (list, tuple)):
            raise TypeError("Input must be a list or tuple.")
        result = []
        for item in sequence:
            if not isinstance(item, (int, float)) and not hasattr(item, '__float__'):
                continue
            try:
                value = math.copysign(1.0, float(item)) * abs(float(item))
                if value < 0:
                    raise ValueError("Value is negative.")
                result.append(value)
            except (TypeError, ValueError):
                pass
        return tuple(result)
    except Exception as e:
        print(f"Error processing sequence: {e}")
        return None
if __name__ == '__main__':
    sample_data = [10, -5.2, "abc", 3.14, True, False]
    output = filter_non_negative(sample_data)
    if output is not None:
        print(output)