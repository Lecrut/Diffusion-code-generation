def union_lists(list1, list2):
    seen = set()
    result = []
    for item in list1 + list2:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

if __name__ == '__main__':
    print(union_lists([1, 2, 3], [3, 4, 5]))