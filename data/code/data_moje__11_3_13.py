def safe_last(lst, default=None):
    if not lst:
        return default
    return lst[-1]

if __name__ == '__main__':
    data = [10, 20, 30, 40, 50]
    empty = []
    print(safe_last(data))
    print(safe_last(empty, "No elements"))
    print(safe_last(["apple", "banana"], "Default"))
    print(safe_last([]))