class EmptyDataError(Exception):
    def __init__(self, message="No data points provided"):
        super().__init__(message)

def _convert_to_float(value):
    if isinstance(value, bool):
        raise TypeError("Boolean values are not accepted as numeric data.")
    if not isinstance(value, (int, float)):
        raise TypeError(f"Invalid data type found: {type(value).__name__}")
    return float(value)

def _find_max(values):
    current_max = None
    for val in values:
        if current_max is None or val > current_max:
            current_max = val
    return current_max

def extract_max_float(data_points: tuple) -> float:
    if not data_points:
        raise EmptyDataError("The input tuple is empty.")
    converted_values = []
    for item in data_points:
        converted_values.append(_convert_to_float(item))
    result = _find_max(converted_values)
    return result

if __name__ == '__main__':
    sample_data = (10.5, 2.8, -1.2, 99.99, 45.0)
    result = extract_max_float(sample_data)
    print(result)