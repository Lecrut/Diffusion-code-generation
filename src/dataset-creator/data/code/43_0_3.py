def remove_by_index(lst: list, index: int) -> bool:
    try:
        lst.pop(index)
        return True
    except IndexError:
        return False
def remove_by_value(lst: list, value) -> bool:
    if value in lst:
        lst.remove(value)
        return True
    return False
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    if remove_by_index(sample_list, 2):
        print(f"Removed item at index 2. List: {sample_list}")
    sample_list = [10, 20, 30, 40]
    if remove_by_value(sample_list, 30):
        print(f"Removed item with value 30. List: {sample_list}")
    sample_list = [10, 20, 40]
    if not remove_by_index(sample_list, -5):
        print("Index out of range.")