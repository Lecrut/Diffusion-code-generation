def find_max(iterable):
    if not iterable:
        return None
    maximum = iterable[0]
    for number in iterable:
        if number > maximum:
            maximum = number
    return maximum

if __name__ == '__main__':
    list1 = [10, 5, 20, 8, 15]
    tuple2 = (3, -1, 99, 42)
    empty_list = []
    print(f"Maximum of {list1}: {find_max(list1)}")
    print(f"Maximum of {tuple2}: {find_max(tuple2)}")
    print(f"Maximum of {empty_list}: {find_max(empty_list)}")