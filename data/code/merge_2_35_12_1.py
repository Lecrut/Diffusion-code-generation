import bisect
def find_target(sorted_list: list[int], target: int) -> bool | None:
    index = bisect.bisect_left(sorted_list, target)
    if index < len(sorted_list) and sorted_list[index] == target:
        return True
    else:
        return False
if __name__ == '__main__':
    data = [10, 23, 45, 67, 89, 102]
    query = 67
    if find_target(data, query):
        print(query)
    else:
        print("Not found")