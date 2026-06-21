def get_first_element(lst):
    try:
        return lst[0]
    except IndexError as e:
        raise ValueError("List is empty") from e

if __name__ == '__main__':
    sample_list = [7, 14, 21, 28]
    print(get_first_element(sample_list))