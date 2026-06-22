class DifferenceFinder:
    def __init__(self, list_a: list[float], list_b: list[float]):
        if len(list_a) != len(list_b):
            raise ValueError("Input lists must have the same length")
        self.list_a = list_a
        self.list_b = list_b

    def find_first_zero_difference_index(self) -> int:
        for index, (a, b) in enumerate(zip(self.list_a, self.list_b)):
            if a - b == 0:
                return index
        return -1

if __name__ == '__main__':
    list_a = [1.0, 2.5, 3.14, 4.0]
    list_b = [0.5, 2.0, 3.14, 3.9]
    finder = DifferenceFinder(list_a, list_b)
    index = finder.find_first_zero_difference_index()
    print(index)