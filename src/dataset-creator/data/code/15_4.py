from typing import Callable, List
def create_sorter(stable: bool = True) -> Callable[[List[float]], List[float]]:
    def sorter(numbers: List[float]) -> List[float]:
        if stable:
            sorted_numbers = sorted(numbers)
        else:
            sorted_numbers = sorted(numbers, key=lambda x: -x)
        return sorted_numbers
    return sorter
if __name__ == '__main__':
    sample_data: List[float] = [3.14, 2.71, 1.41, 0.58, 9.99]
    stable_sorter: Callable[[List[float]], List[float]] = create_sorter(stable=True)
    unstable_sorter: Callable[[List[float]], List[float]] = create_sorter(stable=False)
    result_stable: List[float] = stable_sorter(sample_data.copy())
    result_unstable: List[float] = unstable_sorter(sample_data.copy())
    print(result_stable)
    print(result_unstable)