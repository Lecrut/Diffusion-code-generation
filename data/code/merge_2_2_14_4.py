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
    arr_np = np.array([1, 2, 3])
    arr_mixed = np.array([-1, 0, 4])
    import pandas as pd
    s_series = pd.Series([1.5, -2.0, 3.7])
    print(f"NumPy array {arr_np}: {is_positive(arr_np)}")
    print(f"Mixed NumPy array {arr_mixed}: {is_positive(arr_mixed)}")
    print(f"Pandas Series {s_series.tolist()}: {is_positive(s_series)}")