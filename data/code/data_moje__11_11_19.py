def get_and_remove_last(lst):
    if not lst:
        return None
    return lst.pop()

if __name__ == '__main__':
    data = [10, 20, 30]
    result = get_and_remove_last(data)
    print(result)