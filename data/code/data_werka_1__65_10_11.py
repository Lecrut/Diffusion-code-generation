def get_sublist(lst):
    try:
        return lst[2:5]
    except TypeError:
        raise ValueError("Input must be a list")

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    print(get_sublist(sample_list))