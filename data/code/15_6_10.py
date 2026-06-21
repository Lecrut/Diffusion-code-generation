def get_penultimate_element(lst):
    length = len(lst)
    if length < 2:
        raise IndexError("List must contain at least two elements")
    index = length - 2
    return lst[index]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = get_penultimate_element(sample_list)
    print(result)