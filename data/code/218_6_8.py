from typing import List

class MinFinder:
    def __init__(self, data: List[int]):
        self.data = data

    def find_minimum(self) -> int:
        if not self.data:
            raise ValueError("Empty list provided")
        current_min = self.data[0]
        for element in self.data[1:]:
            if element < current_min:
                current_min = element
        return current_min

if __name__ == '__main__':
    min_finder_1 = MinFinder([5, 2, 8, 1, 9, 3])
    print("Minimum in first list:", min_finder_1.find_minimum())

    min_finder_2 = MinFinder([42, 10, 55, 33])
    print("Minimum in second list:", min_finder_2.find_minimum())