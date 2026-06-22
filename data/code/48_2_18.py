import sys
from typing import Tuple, Any

EMPTY_SEQUENCE_ERROR_MESSAGE = "Cannot extract maximum from an empty sequence."
TYPE_ERROR_MESSAGE_TEMPLATE = "Expected numeric type, got {}"
INVALID_FLOAT_CONSTANT = float('inf')

class EmptySequenceError(Exception):
    def __init__(self, msg):
        super(EmptySequenceError, self).__init__(msg)

def _check_numeric_type(value):
    if isinstance(value, bool):
        raise TypeError(TYPE_ERROR_MESSAGE_TEMPLATE.format(type(value).__name__))
    if not isinstance(value, (int, float)):
        raise TypeError(TYPE_ERROR_MESSAGE_TEMPLATE.format(type(value).__name__))
    return float(value)

def find_maximum_value(data_points: Tuple[Any, ...]) -> float:
    if len(data_points) == 0:
        raise EmptySequenceError(EMPTY_SEQUENCE_ERROR_MESSAGE)
    
    current_max = None
    
    for point in data_points:
        numeric_val = _check_numeric_type(point)
        
        if current_max is None:
            current_max = numeric_val
        else:
            if numeric_val > current_max:
                current_max = numeric_val
                
    return current_max

def _get_sample_data() -> Tuple:
    return (1.1, 2.2, 3.3, 4.4, 5.5, 0.0, -1.1)

if __name__ == '__main__':
    test_data = _get_sample_data()
    result_value = find_maximum_value(test_data)
    print(result_value)