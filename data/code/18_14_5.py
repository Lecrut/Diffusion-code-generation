def get_middle_value(lst):
    if not lst:
        raise ValueError("List must not be empty")
    n = len(lst)
    mid_index = n // 2
    if n % 2 == 0:
        return (lst[mid_index - 1] + lst[mid_index]) / 2
    else:
        return lst[mid_index]

if __name__ == '__main__':
    sample_data = [1, 3, 5, 7, 9]
    result = get_middle_value(sample_data)
    print(result)