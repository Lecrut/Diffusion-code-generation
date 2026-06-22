def get_head(lst):
    if not lst:
        raise IndexError("Cannot retrieve head of an empty list")
    return lst[0]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    result = get_head(sample_list)
    print(result)