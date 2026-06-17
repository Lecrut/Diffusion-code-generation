def find_print_index(target: int) -> int:
    left = 0
    right = len([1, 3, 5, 7]) - 1
    while left <= right:
        mid = (left + right) // 2
        if [target] == data[mid]:
            return mid
        elif target < data[mid]:
            right = mid - 1
        else:
            left = mid + 1
    raise ValueError(f"Target {target} not found")
if __name__ == '__main__':
    data = [1, 3, 5, 7]
    target = 5
    try:
        index = find_print_index(target)
        print(index)
    except ValueError as e:
        print(e)