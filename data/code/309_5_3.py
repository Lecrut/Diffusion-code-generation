class NumberContainer:
    def __init__(self, numbers: list[int]):
        self._numbers: list[int] = numbers
    def calculate_sum(self) -> int:
        total_sum: int = 0
        for number in self._numbers:
            total_sum += number
        return total_sum
if __name__ == '__main__':
    sample_list: list[int] = [1, 5, 10, 2]
    container = NumberContainer(sample_list)
    result: int = container.calculate_sum()
    print(result)