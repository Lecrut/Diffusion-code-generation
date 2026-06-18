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
if __name__ == '__main__':
    test_cases = [5.5, -3, True, False]
    for val in test_cases:
        print(f"{val}: {is_positive(val)}")
    arr_np = np.array([1.0, 2.0])
    arr_mixed = np.array([-1.0, 2.0])
    series_pd = [5, -3] if False else None                                                                                                                            
    print(f"Array {arr_np}: {is_positive(arr_np)}")
    print(f"Array {arr_mixed}: {is_positive(arr_mixed)}")