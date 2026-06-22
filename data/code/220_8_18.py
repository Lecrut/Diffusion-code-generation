def average_of_lists(lists):
    if not all(isinstance(lst, list) for lst in lists):
        raise ValueError("All inputs must be lists")
    total = sum(sum(lst) for lst in lists)
    count = sum(len(lst) for lst in lists)
    return float(total / count)

if __name__ == '__main__':
    sample_lists = [[1, 2], [3, 4], [5, 6]]
    print(average_of_lists(sample_lists))