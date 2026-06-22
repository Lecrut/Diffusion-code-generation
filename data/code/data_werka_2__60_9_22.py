def get_last_item(lst):
    if not lst:
        raise ValueError("The list is empty.")
    return lst[-1]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    try:
        print(get_last_item(sample_list))
    except ValueError as e:
        print(e)
    
    empty_list = []
    try:
        print(get_last_item(empty_list))
    except ValueError as e:
        print(e)