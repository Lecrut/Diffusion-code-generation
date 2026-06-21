def get_penultimate(lst):
    if len(lst) < 2:
        raise IndexError("List must contain at least two elements")
    return lst[-2]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = get_penultimate(sample_list)
    print(result)