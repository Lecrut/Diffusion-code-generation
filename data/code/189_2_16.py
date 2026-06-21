def remove_by_index(lst, index):
    n = len(lst)
    if not (0 <= index < n):
        raise IndexError("Index out of bounds")
    del lst[index]
    return lst

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    print("Initial list:", sample_list)
    try:
        sample_list = remove_by_index(sample_list, 2)
        print("After removing index 2:", sample_list)
        sample_list = remove_by_index(sample_list, 0)
        print("After removing index 0:", sample_list)
        sample_list = remove_by_index(sample_list, 10)
    except IndexError as e:
        print("Error caught:", e)