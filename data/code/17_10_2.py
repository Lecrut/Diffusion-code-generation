def get_last_element(items):
    if len(items) == 0:
        return None
    return items[-1]

if __name__ == '__main__':
    print(get_last_element([1, 2, 3, 4]))
    print(get_last_element([]))