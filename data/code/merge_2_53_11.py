from typing import Iterable
def count_elements(sequence: Iterable) -> int:
    return sum(1 for _ in sequence)
if __name__ == '__main__':
    sample_sequence = [1, 2, 3, 4, 5]
    result = count_elements(sample_sequence)
    print(result)