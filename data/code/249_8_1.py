def find_largest(data):
    if not data:
        return None
    largest = data[0]
    for item in data[1:]:
        if isinstance(largest, str) and isinstance(item, int):
            continue
        if isinstance(largest, int) and isinstance(item, str):
            continue
        if isinstance(largest, int) and isinstance(item, int):
            if item > largest:
                largest = item
        elif isinstance(largest, str) and isinstance(item, str):
            if item > largest:
                largest = item
        else:
            try:
                str_largest = str(largest)
                str_item = str(item)
                if str_item > str_largest:
                    largest = item
            except Exception:
                pass
    return largest
if __name__ == '__main__':
    list1 = [10, "apple", 5, "zebra", 20]
    print(f"List 1: {list1}")
    result1 = find_largest(list1)
    print(f"Largest item in List 1: {result1}")
    list2 = ["banana", 100, "apple", 50]
    print(f"\nList 2: {list2}")
    result2 = find_largest(list2)
    print(f"Largest item in List 2: {result2}")
    list3 = [3.14, "hello", 2.718]
    print(f"\nList 3: {list3}")
    result3 = find_largest(list3)
    print(f"Largest item in List 3: {result3}")
    list4 = ["a", "b", "c"]
    print(f"\nList 4: {list4}")
    result4 = find_largest(list4)
    print(f"Largest item in List 4: {result4}")
    list5 = []
    print(f"\nList 5: {list5}")
    result5 = find_largest(list5)
    print(f"Largest item in List 5: {result5}")