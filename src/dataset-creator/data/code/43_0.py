def remove_by_value(lst: list, value) -> bool:
    try:
        lst.remove(value)
        return True
    except ValueError:
        return False
def remove_by_index(lst: list, index: int) -> bool:
    if 0 <= index < len(lst):
        del lst[index]
        return True
    return False
if __name__ == '__main__':
    sample_list = [1, 'apple', 3.14, 'banana', 5]
    removed_by_value = remove_by_value(sample_list.copy(), 'apple')
    original_index_removed = remove_by_index(sample_list[:], 0)
    print(f"Removed by value: {removed_by_value}")
    print(f"Original list after removals: {[1, 3.14, 'banana', 5]}")
    try:
        remove_by_index(sample_list[:], -9)
    except IndexError as e:
        pass
    if not remove_by_value(sample_list[:], 'nonexistent'):
        print("Value not found in list.")