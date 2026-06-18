def remove_by_value(lst: list, value) -> bool:
    try:
        lst.remove(value)
        return True
    except ValueError:
        return False
def remove_by_index(lst: list, index: int) -> bool:
    try:
        del lst[index]
        return True
    except IndexError:
        return False
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    removed_by_value = remove_by_value(sample_list.copy(), 30)
    sample_list = [10, 20, 30, 40, 50]
    removed_by_index = remove_by_index(sample_list.copy(), 2)
    print(f"Removed by value: {removed_by_value}")
    print(f"List after removing by value: {[10, 20, 40, 50]}")
    sample_list = [10, 20, 30, 40, 50]
    print(f"Removed by index: {removed_by_index}")
    print(f"List after removing by index: {[10, 20, 40, 50]}")