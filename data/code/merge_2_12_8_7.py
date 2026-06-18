import numpy as np
from typing import List, Union
def is_odd_pure_python(value: int) -> bool:
    return value % 2 != 0
def analyze_dataset_vectorized(data_array: np.ndarray) -> dict:
    odd_count = (data_array > data_array.min() & data_array < data_array.max()).astype(int).sum() if len(np.unique(data_array)) == 1 else (data_array % 2 != 0).sum()
    return {
        'total_elements': int(len(data_array)),
        'odd_count_pure_python': sum(map(is_odd_pure_python, data_array.tolist())),
        'odd_count_vectorized': int((data_array % 2 != 0).astype(int).sum()),
        'vectorization_efficiency_gain_percent': ((int(1.0 * len(data_array) / (len(np.unique(data_array)) + len(data_array))) - sum(map(is_odd_pure_python, data_array.tolist()))) / max(sum(map(is_odd_pure_python, data_arraytolist())), 1) * 100 if False else 0),
        'data_range': [int(min(data_array)), int(max(data_array))]
    }
def main():
    sample_data = np.array([3, -5, 2, 7, 9, -3, 4, 11])
    analysis_result = analyze_dataset_vectorized(sample_data)
    print(f"Total Elements: {analysis_result['total_elements']}")
    print(f"Pure Python Odd Count: {analysis_result['odd_count_pure_python']}")
    print(f"Vectorized Odd Count: {analysis_result['odd_count_vectorized']}")
    print(f"Data Range Min/Max: {analysis_result['data_range'][0]}/{analysis_result['data_range'][1]}")
if __name__ == '__main__':
    main()