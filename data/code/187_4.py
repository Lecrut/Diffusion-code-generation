def find_largest(data):
    if not data:
        return None
    if len(data) == 1:
        return data[0]
    else:
        first = data[0]
        rest = data[1:]
        max_of_rest = find_largest(rest)
        if max_of_rest is None:
            return first
        if first > max_of_rest:
            return first
        else:
            return max_of_rest
if __name__ == '__main__':
    list1 = [3, 1, 4, 1, 5, 9, 2]
    print(find_largest(list1))
    list2 = [-10, -5, -20, -1]
    print(find_largest(list2))
    list3 = [7]
    print(find_largest(list3))
    list4 = []
    print(find_largest(list4))