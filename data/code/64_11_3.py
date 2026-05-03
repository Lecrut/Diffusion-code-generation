def find_final_item_index(item_indices):
    if not item_indices:
        raise IndexError("Input list of indices cannot be empty")
    return item_indices[-1]
if __name__ == '__main__':
    list1 = [1, 5, 9, 12]
    result1 = find_final_item_index(list1)
    print(f"Result for {list1}: {result1}")
    list2 = [100]
    result2 = find_final_item_index(list2)
    print(f"Result for {list2}: {result2}")
    list3 = [42]
    result3 = find_final_item_index(list3)
    print(f"Result for {list3}: {result3}")
    list4 = []
    try:
        result4 = find_final_item_index(list4)
        print(f"Result for {list4}: {result4}")
    except IndexError as e:
        print(f"Error for {list4}: {e}")