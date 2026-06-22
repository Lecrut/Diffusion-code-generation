def get_last_item(lst):
    if not lst:
        return None
    return lst.pop()

if __name__ == '__main__':
    result = get_last_item([1, 2, 3])
    print(result)
    result = get_last_item([])
    print(result)