import functools
def find_largest(data):
    if not data:
        return None
    def compare(a, b):
        if isinstance(a, str) and isinstance(b, str):
            if a > b:
                return 1
            elif a < b:
                return -1
            else:
                return 0
        elif isinstance(a, int) and isinstance(b, int):
            if a > b:
                return 1
            elif a < b:
                return -1
            else:
                return 0
        elif isinstance(a, int):
            return -1
        elif isinstance(b, int):
            return 1
        else:
            return 0
    largest = data[0]
    for item in data[1:]:
        if compare(item, largest) == 1:
            largest = item
    return largest
if __name__ == '__main__':
    list1 = [10, "apple", 5, "zebra", 20]
    result1 = find_largest(list1)
    print(f"List: {list1}")
    print(f"Largest item: {result1}")
    list2 = ["banana", "apple", "date", "cherry"]
    result2 = find_largest(list2)
    print(f"\nList: {list2}")
    print(f"Largest item: {result2}")
    list3 = [50, 100, "a", "z"]
    result3 = find_largest(list3)
    print(f"\nList: {list3}")
    print(f"Largest item: {result3}")
    list4 = ["cat", 100, "dog"]
    result4 = find_largest(list4)
    print(f"\nList: {list4}")
    print(f"Largest item: {result4}")
    list5 = []
    result5 = find_largest(list5)
    print(f"\nList: {list5}")
    print(f"Largest item: {result5}")