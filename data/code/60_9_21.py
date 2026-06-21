def get_last_item(lst):
    if not lst:
        raise ValueError("The list is empty.")
    return lst[-1]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    try:
        last_element = get_last_item(sample_list)
        print(f"The list of numbers is: {sample_list}")
        print(f"The last element in the list is: {last_element}")
    except ValueError as e:
        print(e)

    empty_list = []
    try:
        last_element = get_last_item(empty_list)
        print(f"The list of numbers is: {empty_list}")
        print(f"The last element in the list is: {last_element}")
    except ValueError as e:
        print(e)