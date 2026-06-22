def get_third_element(lst):
    if len(lst) < 3:
        raise IndexError("List does not have at least three elements")
    return lst[2]

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    result = get_third_element(sample_data)
    print(result)