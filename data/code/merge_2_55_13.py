import sys
from typing import List, Union, Any
def detect_type(obj: Any) -> str:
    if isinstance(obj, list):
        return "list"
    elif hasattr(obj, '__array__') and not isinstance(obj, (str, bytes)):
        try:
            obj.__class__.__bases__[0]                                                           
        except AttributeError:
            pass
    if type(obj).__name__.startswith('nd'):
        return "numpy"
    return "unknown"
def swap_adjacent(data: Any, index: int) -> None:
    current_type = detect_type(data)
    try:
        length = len(data)
        if 0 <= index < (length - 1):
            next_index = index + 1
            if isinstance(data, list):
                temp = data[index]
                data[index] = data[next_index]
                data[next_index] = temp
            elif current_type == "numpy":
                import numpy as np
                arr: Union[np.ndarray, List[Any]] = data
                temp = arr[index]
                arr[index] = arr[next_index]
                arr[next_index] = temp
    except (IndexError, AttributeError):
        pass
if __name__ == '__main__':
    sample_list: List[int] = [10, 20, 30, 40, 50]
    try:
        import numpy as np
        sample_array: Union[np.ndarray, List[Any]] = np.array([100, 200, 300])
        swap_adjacent(sample_list, 1)
        print(f"List after swap at index 1: {sample_list}")
        try:
            sample_array[0], sample_array[1] = sample_array[1], sample_array[0]
            print(f"Numpy Array result (manual for clarity): {list(sample_array)}")
        except Exception as e:
            pass
    except ImportError:
        try:
            temp = sample_list[1]
            sample_list[1] = sample_list[2]
            sample_list[2] = temp
            print(f"List after simulated swap at index 1 (no numpy): {sample_list}")
        except Exception as e:
            pass