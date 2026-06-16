import numpy as np
import pandas as pd
def check_positivity(value):
    try:
        val = float(value)
        return val > 0
    except (ValueError, TypeError):
        raise ValueError("Input must be convertible to numeric.")
if __name__ == '__main__':
    assert check_positivity(5.0) is True
    assert check_positivity(-3.14) is False
    arr = np.array([1.2, -2.5, 0.0])
    expected_arr = [True, False, False]
    assert all(check_positivity(x) == e for x, e in zip(arr, expected_arr))
    s = pd.Series([-1, 4, np.nan])
    result_s = list(map(lambda x: check_positivity(x), s.dropna()))
    expected_s = [False, True]
    assert result_s == expected_s