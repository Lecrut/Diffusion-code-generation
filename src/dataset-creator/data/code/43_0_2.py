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
    original_length = len(sample_list)
    sample_list.remove(1)
    removed_by_index = remove_by_index(sample_list, 0)
    print(f"List after operations: {sample_list}")
    print(f"Removed 'apple' successfully? {removed_by_value}")
    print(f"Removed element at index 0 successfully? {removed_by_index}")