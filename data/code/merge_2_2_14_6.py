import numpy as np
from typing import Union
def is_positive(value: Union[int, float, np.ndarray]) -> bool:
    if isinstance(value, (int, float)):
        return value > 0
    elif hasattr(value, '__iter__') and not isinstance(value, str):
        try:
            arr = np.asarray(value)
            return np.all(arr > 0)
        except Exception:
            raise TypeError("Input must be a numeric scalar or array-like.")
    else:
        raise TypeError(f"Unsupported type {type(value).__name__}.")
if __name__ == '__main__':
    test_cases = [5, -3.2, 0, np.array([1, 2]), np.array([-1, 2])]
    for case in test_cases:
        print(f"Input: {case}, Is Positive: {is_positive(case)}")