def find_largest(data):
    if not data:
        raise ValueError("List cannot be empty")
    if len(data) == 1:
        return data[0]
    else:
        first = data[0]
        rest = data[1:]
        largest_of_rest = find_largest(rest)
        if first > largest_of_rest:
            return first
        else:
            return largest_of_rest
if __name__ == '__main__':
    list1 = [10, 5, 20, 8, 15]
    print(find_largest(list1))
    list2 = [-5, -1, -10, -3]
    print(find_largest(list2))
    list3 = [42]
    print(find_largest(list3))
    list4 = [100]
    print(find_largest(list4))