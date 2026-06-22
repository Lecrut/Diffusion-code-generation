class EmptySequenceError(Exception):
    def __init__(self, message="The sequence of data points is empty."):
        super().__init__(message)

def extract_max_float(data_points: tuple) -> float:
    if not data_points:
        raise EmptySequenceError("The sequence of data points is empty.")
    max_value = None
    for value in data_points:
        if not isinstance(value, (int, float)):
            raise TypeError(f"Invalid type in data points: {type(value)}")
        if max_value is None or value > max_value:
            max_value = value
    return float(max_value)

if __name__ == '__main__':
    sample_data = (3.14, 2.71, 9.81, 4.5)
    print(extract_max_float(sample_data))