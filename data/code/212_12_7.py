from typing import Iterable, Tuple, Optional

class MinMaxAnalyzer:
    @staticmethod
    def analyze(numbers: Iterable) -> Tuple[Optional[int], Optional[int]]:
        try:
            iterator = iter(numbers)
            first = next(iterator)
            min_val = max_val = first
            for item in iterator:
                if item < min_val:
                    min_val = item
                elif item > max_val:
                    max_val = item
            return (min_val, max_val)
        except StopIteration:
            return (None, None)

if __name__ == '__main__':
    sample_numbers = [15, 8, 22, 4, 30, 11]
    analyzer = MinMaxAnalyzer()
    min_val, max_val = analyzer.analyze(sample_numbers)
    print(f"Minimum: {min_val}")
    print(f"Maximum: {max_val}")