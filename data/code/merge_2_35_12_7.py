import bisect
def find_target(sorted_list: list, target) -> int | None:
    index = bisect.bisect_left(sorted_list, target)
    if index < len(sorted_list) and sorted_list[index] == target:
        return index
    return None
if __name__ == '__main__':
    data = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    query = 7
    result = find_target(data, query)
    if result is not None:
        print(result)
    else:
        print("Target not found")