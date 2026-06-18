def remove_by_index(lst: list, index: int) -> None:
    if 0 <= index < len(lst):
        del lst[index]
def remove_by_value(lst: list, value) -> bool:
    try:
        lst.remove(value)
        return True
    except ValueError:
        return False
if __name__ == '__main__':
    data = [10, 20, 30, 40, 50]
    remove_by_index(data, 2)
    sample_data = ['apple', 'banana', 'cherry']
    if not remove_by_value(sample_data, 'banana'):
        print("Value not found.")
    else:
        print(f"Removed item. List is now {sample_data}")
    print(f"List after index removal: {data}")