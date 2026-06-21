from typing import List

class MaxFinder:
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
    finder = MaxFinder()
    sample_list_int = [7, 14, 21, 28, 35]
    result_int = finder.find_maximum(sample_list_int)
    print(f"The maximum element in {sample_list_int} is: {result_int}")