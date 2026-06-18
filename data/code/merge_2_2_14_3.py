import numpy as np
from typing import Union, List
def is_positive(value: Union[int, float, np.ndarray, 'pd.Series']) -> bool:
    try:
        arr = np.asarray(value)
        return (arr > 0).all()
    except Exception:
        raise TypeError("Input must be a scalar or array-like")
if __name__ == '__main__':
    import pandas as pd
    assert is_positive(1.5)
    assert not is_positive(-2.3)
    arr_pos = np.array([1, 2, 3])
    arr_neg = np.array([-1, -2, -3])
    arr_mixed = np.array([0, -1, 5])
    assert is_positive(arr_pos)
    assert not is_positive(arr_neg)
    assert not is_positive(arr_mixed)
    series_pos = pd.Series([1.0, 2.0, 3.0])
    series_mix = pd.Series([-5.0, 0.0, 4.0])
    assert is_positive(series_pos)
    assert not is_positive(series_mix)