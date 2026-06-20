class ArithmeticSeries:
    @staticmethod
    def sum_range(start: int, end: int) -> int:
        return (end - start + 1) * (start + end) // 2

if __name__ == '__main__':
    series = ArithmeticSeries()
    result = series.sum_range(1, 10)
    print(result)
    another_result = series.sum_range(5, 15)
    print(another_result)