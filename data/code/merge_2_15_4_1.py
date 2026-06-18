from typing import Callable, List
def create_sorter(stable: bool = True) -> Callable[[List[float]], List[float]]:
    def sorter(numbers: List[float]) -> List[float]:
        return sorted(numbers, key=lambda x: -x if stable else x)
    return sorter
if __name__ == '__main__':
    data = [3.14, 2.71, 1.618]
    unstable_sorter = create_sorter(stable=False)
    sorted_data = unstable_sorter(data.copy())
    print(sorted_data)