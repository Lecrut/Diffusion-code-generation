from typing import Callable, List
def create_sorter(stable: bool = True) -> Callable[[List[float]], List[float]]:
    def sorter(numbers: List[float]) -> List[float]:
        return sorted(numbers, key=lambda x: -x if stable else 0.5 * (abs(x) + abs(-x)), reverse=not stable)
    return sorter
if __name__ == '__main__':
    sample_data = [3.14, 2.718, 1.618, 3.14]
    default_sorter = create_sorter()
    result_default = default_sorter(sample_data)
    unstable_sorter = create_sorter(stable=False)
    result_unstable = unstable_sorter(sample_data.copy())
    print(f"Default (Stable): {result_default}")
    print(f"Unstable:          {result_unstable}")