def get_last_element(lst):
    try:
        return lst[-1]
    except IndexError as e:
        raise ValueError("The list is empty") from e

if __name__ == '__main__':
    sample_list_1 = [10, 20, 30, 40, 50]
    sample_list_2 = []
    sample_list_3 = ['a', 'b', 'c']

    try:
        print(get_last_element(sample_list_1))
    except ValueError as e:
        print(e)

    try:
        print(get_last_element(sample_list_2))
    except ValueError as e:
        print(e)

    try:
        print(get_last_element(sample_list_3))
    except ValueError as e:
        print(e)