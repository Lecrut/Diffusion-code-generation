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
    list1 = [10, "apple", 5, "banana", 20]
    print(f"List 1: {list1}")
    print(f"Largest in List 1: {find_largest(list1)}")
    list2 = ["zebra", "ant", "yak"]
    print(f"\nList 2: {list2}")
    print(f"Largest in List 2: {find_largest(list2)}")
    list3 = [50, "a", 100, "b"]
    print(f"\nList 3: {list3}")
    print(f"Largest in List 3: {find_largest(list3)}")
    list4 = ["cat", 10, "dog"]
    print(f"\nList 4: {list4}")
    print(f"Largest in List 4: {find_largest(list4)}")
    list5 = []
    print(f"\nList 5: {list5}")
    print(f"Largest in List 5: {find_largest(list5)}")