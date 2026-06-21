def get_last_item(lst):
    if not lst:
        raise ValueError("The list is empty.")
    return lst[-1]

if __name__ == '__main__':
    SAMPLE_LIST = [10, 20, 30, 40, 50]
    EMPTY_LIST = []

    try:
        print("Last item of SAMPLE_LIST:", get_last_item(SAMPLE_LIST))
    except ValueError as e:
        print(e)

    try:
        print("Last item of EMPTY_LIST:", get_last_item(EMPTY_LIST))
    except ValueError as e:
        print(e)