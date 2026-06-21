def get_second_last(items):
    if len(items) < 2:
        raise IndexError("List must contain at least two elements")
    return items[-2]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    print(get_second_last(sample_list))