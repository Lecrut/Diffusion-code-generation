def get_last_element(items):
    if not items:
        raise IndexError("Cannot extract last element from an empty list")
    return items[-1:]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = get_last_element(sample_list)
    print(result[0])