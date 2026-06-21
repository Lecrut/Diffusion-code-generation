from typing import List

class MaxFinder:
    MAX_LIST = [7, 14, 21, 28, 35]

    @staticmethod
    def find_maximum(data: List[int]) -> int:
        if not data:
            raise ValueError("Input list cannot be empty")
        maximum = data[0]
        for element in data[1:]:
            if element > maximum:
                maximum = element
        return maximum

if __name__ == '__main__':
    result = MaxFinder.find_maximum(MaxFinder.MAX_LIST)
    print(f"The maximum element in {MaxFinder.MAX_LIST} is: {result}")