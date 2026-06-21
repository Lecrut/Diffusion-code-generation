def get_penultimate(lst):
    length = len(lst)
    if length < 2:
        raise ValueError("List must have at least two elements")
    index = length - 2
    return lst[index]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = get_penultimate(sample_list)
    print(result)