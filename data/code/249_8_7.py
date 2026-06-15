def find_largest(data):
    if not data:
        return None
    largest = data[0]
    for item in data[1:]:
        if isinstance(largest, str) and isinstance(item, str):
            if item > largest:
                largest = item
        elif isinstance(item, str) and not isinstance(largest, str):
            largest = item
        elif isinstance(largest, str) and not isinstance(item, str):
            pass 
        elif isinstance(largest, int) and isinstance(item, str):
            largest = item
        elif isinstance(largest, int) and isinstance(item, int):
            if item > largest:
                largest = item
        elif isinstance(item, int) and not isinstance(largest, (int, str)):
             largest = item
    return largest
if __name__ == '__main__':
    list1 = [10, 5, "hello", 20]
    print(f"List: {list1}, Largest: {find_largest(list1)}")
    list2 = ["apple", "zebra", "banana"]
    print(f"List: {list2}, Largest: {find_largest(list2)}")
    list3 = [100, 50, "a", "b", "c"]
    print(f"List: {list3}, Largest: {find_largest(list3)}")
    list4 = ["9", "100", "50"]
    print(f"List: {list4}, Largest: {find_largest(list4)}")
    list5 = [5, 10, -3, 1]
    print(f"List: {list5}, Largest: {find_largest(list5)}")
    list6 = []
    print(f"List: {list6}, Largest: {find_largest(list6)}")