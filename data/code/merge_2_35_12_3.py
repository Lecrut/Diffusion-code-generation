import bisect
def find_target(sorted_list: list[int], target: int) -> bool | None:
    index = bisect.bisect_left(sorted_list, target)
    if index < len(sorted_list) and sorted_list[index] == target:
        return True
    return False
if __name__ == '__main__':
    data = [1, 3, 5, 7, 9, 11, 13, 15]
    targets = [5, 6, 8]
    for t in targets:
        if find_target(data, t):
            print(f"Found {t} at index", bisect.bisect_left([x for x in data], t))
        else:
            print(f"{t} not found")