import numpy as np
from typing import Union
def check_positivity(value: Union[int, float, np.ndarray]) -> bool:
    if isinstance(value, (int, float)):
        return value > 0
    elif hasattr(value, 'shape'):
        all_positive = True
        for val in value.flatten():
            if not (val >= 0):
                all_positive = False
                break
        return all_positive
    else:
        raise TypeError("Unsupported input type")
if __name__ == '__main__':
    sample_scalar = -5.0
    sample_array = np.array([1, 2, 3])
    sample_series_data = [4, 5]
    print(check_positivity(sample_scalar))
    print(check_positivity(np.array([-1, -2])))
    print(check_positivity(sample_array))