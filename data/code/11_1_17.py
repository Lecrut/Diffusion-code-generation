def get_last_item(lst):
    if not lst:
        return None
    return lst.pop()

if __name__ == '__main__':
    print(get_last_item([1, 2, 3]))
    print(get_last_item([]))