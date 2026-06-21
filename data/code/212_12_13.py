from typing import Iterable, Tuple, Optional

class MinMaxFinder:
    @staticmethod
    def find_min_max(iterable: Iterable) -> Tuple[Optional[int], Optional[int]]:
        try:
            iterator = iter(iterable)
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
    print(MinMaxFinder.find_min_max([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]))
    print(MinMaxFinder.find_min_max([]))
    print(MinMaxFinder.find_min_max([7]))