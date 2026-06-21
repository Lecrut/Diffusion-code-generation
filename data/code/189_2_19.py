def remove_by_index(lst, index):
    if not (0 <= index < len(lst)):
        raise IndexError("Index out of bounds")
    del lst[index]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    print("Initial list:", sample_list)
    try:
        remove_by_index(sample_list, 2)
        print("After removing index 2:", sample_list)
        remove_by_index(sample_list, 0)
        print("After removing index 0:", sample_list)
        remove_by_index(sample_list, 10)
    except IndexError as e:
        print("Error caught:", e)