def get_final_element(lst):
    if not isinstance(lst, list):
        raise TypeError("Input must be a list")
    if not lst:
        raise ValueError("List must be non-empty")
    return lst[-1]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40]
    result = get_final_element(sample_list)
    print(result)