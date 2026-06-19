def get_last_element(arr):
    try:
        return arr[-1]
    except IndexError as e:
        raise ValueError("The provided list is empty.") from e

if __name__ == '__main__':
    sample_list = [5, 15, 25, 35, 45]
    print(get_last_element(sample_list))