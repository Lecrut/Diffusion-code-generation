def find_middle(lst):
    length = len(lst)
    if length == 0:
        raise ValueError("List must not be empty")
    if length % 2 == 1:
        return lst[length // 2]
    return lst[length // 2 - 1]

if __name__ == '__main__':
    print(find_middle([1, 2, 3]))
    print(find_middle([1, 2, 3, 4]))
    print(find_middle([10]))
    print(find_middle([10, 20]))
    print(find_middle([1, 2, 3, 4, 5, 6]))