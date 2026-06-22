def find_min(lst):
    if not lst:
        raise ValueError("List cannot be empty")
    return min(lst)

if __name__ == '__main__':
    sample_list = [5, 3, 9, 1, 10]
    try:
        print(find_min(sample_list))
    except ValueError as e:
        print(e)