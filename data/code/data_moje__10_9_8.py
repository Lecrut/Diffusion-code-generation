def get_first_element(lst):
    if not lst:
        raise ValueError("List is empty")
    return lst[0]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = get_first_element(sample_list)
    print(result)