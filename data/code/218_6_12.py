from typing import List, Optional

class MinFinder:
    @staticmethod
    def find_minimum(data: List[int]) -> Optional[int]:
        if not data:
            return None
        current_min = data[0]
        for element in data[1:]:
            if element < current_min:
                current_min = element
        return current_min

if __name__ == '__main__':
    sample_list = [5, 2, 8, 1, 9, 3]
    min_value = MinFinder.find_minimum(sample_list)
    print(min_value)