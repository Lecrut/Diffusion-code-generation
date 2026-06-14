def find_smallest(data):
    if not data:
        raise ValueError("List cannot be empty")
    if len(data) == 1:
        return data[0]
    else:
        first = data[0]
        rest = data[1:]
        smallest_of_rest = find_smallest(rest)
        if smallest_of_rest < first:
            return smallest_of_rest
        else:
            return first
if __name__ == '__main__':
    list1 = [5, 2, 8, 1, 9]
    list2 = [100, 42, 3, 77, 15]
    list3 = [5]
    list4 = [9]
    list5 = []
    print(f"Smallest in {list1}: {find_smallest(list1)}")
    print(f"Smallest in {list2}: {find_smallest(list2)}")
    print(f"Smallest in {list3}: {find_smallest(list3)}")
    print(f"Smallest in {list4}: {find_smallest(list4)}")
    try:
        print(f"Smallest in {list5}: {find_smallest(list5)}")
    except ValueError as e:
        print(e)