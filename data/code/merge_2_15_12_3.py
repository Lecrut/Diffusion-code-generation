import timeit
from typing import List, Tuple
def sort_numerical_data(data: List[float]) -> List[float]:
    return sorted(data)
if __name__ == '__main__':
    sample_data = [5.2, 1.8, -3.4, 9.7, 0.5, 6.1]
    result = sort_numerical_data(sample_data.copy())
    print(result)