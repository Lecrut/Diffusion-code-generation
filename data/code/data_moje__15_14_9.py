def get_second_to_last(items):
    if len(items) < 2:
        raise IndexError("List must contain at least two items")
    return items[-2]

if __name__ == "__main__":
    sample_list = [10, 20, 30, 40, 50]
    print(get_second_to_last(sample_list))
    empty_list = []
    try:
        get_second_to_last(empty_list)
    except IndexError as e:
        print(e)