def get_third_element(lst):
    try:
        return lst[2]
    except IndexError as e:
        raise IndexError("List does not have a third element") from e

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    print(get_third_element(sample_list))