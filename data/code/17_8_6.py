def get_last_element(lst):
    if not lst:
        raise ValueError("List is empty")
    return lst[-1]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    result = get_last_element(sample_list)
    print(result)