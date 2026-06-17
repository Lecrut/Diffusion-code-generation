import bisect
def find_target(sorted_list: list, target) -> int:
    index = bisect.bisect_left(sorted_list, target)
    if index < len(sorted_list) and sorted_list[index] == target:
        return index
    return -1
if __name__ == '__main__':
    data = [2, 4, 6, 8, 10, 12, 15, 30, 99]
    targets = [4, 7, 30, 100]
    for t in targets:
        pos = find_target(data, t)
        if pos != -1:
            print(f"Target {t} found at index {pos}")
        else:
            print(f"Target {t} not found")