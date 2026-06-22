from typing import List, Tuple, Optional
import statistics

def validate_data(data: List[float]) -> None:
    if not data:
        raise ValueError("Data list cannot be empty")

def compute_extremes(data_list: List[float]) -> Tuple[Optional[float], Optional[float]]:
    validate_data(data_list)
    minimum = min(data_list)
    maximum = max(data_list)
    return minimum, maximum

if __name__ == '__main__':
    sample_data1 = [1.5, 2.3, 0.8, -1.2, 4.7]
    print(f"List: {sample_data1}, Min: {compute_extremes(sample_data1)}, Max: {compute_extremes(sample_data1)}")
    
    sample_data2 = [-5, -1, -6, -3, -2]
    print(f"List: {sample_data2}, Min: {compute_extremes(sample_data2)}, Max: {compute_extremes(sample_data2)}")
    
    sample_data3 = [42.0]
    print(f"List: {sample_data3}, Min: {compute_extremes(sample_data3)}, Max: {compute_extremes(sample_data3)}")