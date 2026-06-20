def get_sublist(lst, start, end):
    if not isinstance(lst, list) or not all(isinstance(x, int) for x in lst):
        raise ValueError("Input must be a list of integers")
    if not isinstance(start, int) or not isinstance(end, int):
        raise ValueError("Start and end indices must be integers")
    if start < 0 or end >= len(lst):
        raise IndexError("Start and end indices are out of bounds")
    return lst[start:end+1]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    print(f"Sublist from index 1 to 3: {get_sublist(sample_list, 1, 3)}")