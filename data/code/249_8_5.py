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
                str_item = str(item)
                if isinstance(largest, str):
                    if str_item > largest:
                        largest = str_item
                else:
                    if str_item > str(largest):
                        largest = str_item
            except Exception:
                pass
    return largest
if __name__ == '__main__':
    list1 = [10, "apple", 5, "banana", 20]
    print(f"List: {list1}, Largest: {find_largest(list1)}")
    list2 = ["zebra", 100, "antelope", 50]
    print(f"List: {list2}, Largest: {find_largest(list2)}")
    list3 = [3.14, "hello", 2.718]
    print(f"List: {list3}, Largest: {find_largest(list3)}")
    list4 = ["a", "b", "c"]
    print(f"List: {list4}, Largest: {find_largest(list4)}")
    list5 = []
    print(f"List: {list5}, Largest: {find_largest(list5)}")
    list6 = [1, 2, -5, "10"]
    print(f"List: {list6}, Largest: {find_largest(list6)}")