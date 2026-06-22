def get_second_to_last(items):
    if len(items) < 2:
        raise IndexError("List must contain at least two elements")
    return items[-2]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = get_second_to_last(sample_list)
    print(result)