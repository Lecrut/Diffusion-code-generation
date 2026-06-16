def stable_sort(numbers: list) -> list:
    return sorted(numbers)
def unstable_sort(numbers: list) -> list:
    numbers_copy = numbers.copy()
    if len(numbers_copy) > 1:
        for i in range(len(numbers_copy)):
            min_idx = i
            for j in range(i + 1, len(numbers_copy)):
                if numbers_copy[j] < numbers_copy[min_idx]:
                    min_idx = j
            if min_idx != i:
                numbers_copy[i], numbers_copy[min_idx] = numbers_copy[min_idx], numbers_copy[i]
    return numbers_copy
def create_sorter(stable: bool) -> callable:
    if stable:
        return stable_sort
    else:
        return unstable_sort
if __name__ == '__main__':
    sample_data = [5, 2, 8, 1, 9]
    sorted_stable = create_sorter(True)(sample_data)
    print(sorted_stable)
    sorted_unstable = create_sorter(False)(sample_data.copy())
    print(sorted_unstable)