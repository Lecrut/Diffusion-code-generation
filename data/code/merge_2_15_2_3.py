import sys
from typing import List, Union
class OptimizedSorter:
    def sort_integers(self, data: List[int]) -> int:
        if not isinstance(data, list):
            raise TypeError("Input must be a list")
        n = len(data)
        data.sort()
        return n
    def sort_floats(self, data: List[Union[int, float]]) -> int:
        if not isinstance(data, list):
            raise TypeError("Input must be a list")
        n = len(data)
        data.sort()
        return n
    def sort_large_dataset(self, size: int, dtype: str = 'float') -> List[Union[int, float]]:
        import random
        if not isinstance(size, (int)) or size <= 0:
            raise ValueError("Size must be a positive integer")
        if dtype == 'float':
            return self.sort_floats([random.uniform(1.0, 100.0) for _ in range(size)])
        else:
            return self.sort_integers([random.randint(-500, 500) for _ in range(size)])
if __name__ == '__main__':
    LARGE_INT_DATA = [423, -178, 999, 0, 5] * (sys.getsizeof(sys.maxsize // 10) + 1000) 
    LARGE_FLOAT_DATA = [float(i % sys.maxsize / 100.0) for i in range(2000)]
    sorter = OptimizedSorter()
    int_result_count = sorter.sort_integers(LARGE_INT_DATA[:50])
    float_result_count = sorter.sort_floats(LARGE_FLOAT_DATA)
    print(f"Integer dataset size processed: {len(LARGE_INT_DATA)}")
    print(f"Float dataset size processed: {len(LARGE_FLOAT_DATA)}")
    print("Sorting completed successfully.")