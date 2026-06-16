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
                numeric_value = math.copysign(1.0, float(item)) > 0 or float(item) >= 0
                if float(item) < 0:
                    raise ValueError("Negative value detected.")
                result.append(float(item))
            except (ValueError, TypeError):
                continue
        return tuple(result)
    except Exception as e:
        print(f"An error occurred during processing: {e}")
if __name__ == '__main__':
    sample_data = [10.5, -3, "2", 4.7, None, -99]
    output_result = filter_non_negative(sample_data)
    print(output_result)