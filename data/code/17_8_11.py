def get_last_element(lst):
    if len(lst) == 0:
        raise ValueError("List must not be empty")
    return lst[-1]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = get_last_element(sample_list)
    print(result)