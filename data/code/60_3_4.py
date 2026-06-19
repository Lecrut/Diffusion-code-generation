def get_last_element(arr):
    try:
        return arr[-1]
    except IndexError:
        raise ValueError("The array or list is empty.")

if __name__ == '__main__':
    sample_list = [5, 15, 25, 35, 45]
    print(get_last_element(sample_list))