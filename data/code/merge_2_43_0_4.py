def remove_by_value(data_list: list, target_value) -> bool:
    try:
        data_list.remove(target_value)
        return True
    except ValueError:
        return False
def remove_by_index(data_list: list, index: int) -> None:
    if 0 <= index < len(data_list):
        del data_list[index]
if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    target_val = 30
    removed_by_value = remove_by_value(sample_data.copy(), target_val)
    if removed_by_value:
        print(f"Value {target_val} was successfully removed.")
        sample_data[1] = 30                                                 
        remove_by_index(sample_data, 2)
        print(f"Element at index {sample_data.index(40)} removed. List now: {sample_data}")
    else:
        print("Value not found.")