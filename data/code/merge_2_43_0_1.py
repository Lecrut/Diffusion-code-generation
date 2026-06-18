def remove_by_index(lst: list, index: int) -> list:
    if 0 <= index < len(lst):
        return lst[:index] + lst[index+1:]
    raise IndexError("Index out of range")
def remove_by_value(lst: list, value) -> list:
    try:
        idx = lst.index(value)
        return lst[:idx] + lst[idx+1:]
    except ValueError:
        print(f"Value {value} not found in list.")
        return lst
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    try:
        updated_by_index = remove_by_index(sample_list.copy(), 2)
        print("Removed by index:", sample_list[:], "->", updated_by_index)
    except IndexError as e:
        print(f"Error removing by index: {e}")
    try:
        updated_by_value = remove_by_value(sample_list.copy(), 30)
        print("Removed by value:", sample_list[:], "->", updated_by_value)
    except ValueError as e:
        pass