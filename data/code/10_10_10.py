def get_first_element(lst):
    try:
        return lst[0]
    except (IndexError, TypeError):
        raise ValueError("Input must be a non-empty list-like object")

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    print(get_first_element(sample_data))