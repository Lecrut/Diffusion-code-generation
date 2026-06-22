def find_middle(lst):
    if not lst:
        raise ValueError("List must not be empty")
    length = len(lst)
    if length % 2 == 0:
        return lst[length // 2 - 1]
    return lst[length // 2]

if __name__ == '__main__':
    print(find_middle([1, 2, 3]))
    print(find_middle([1, 2, 3, 4]))
    print(find_middle([10]))
    print(find_middle([1, 2]))