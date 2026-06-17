def remove_by_index(lst: list, index: int) -> bool:
    if 0 <= index < len(lst):
        lst.pop(index)
        return True
    return False
def remove_by_value(lst: list, value) -> bool:
    try:
        lst.remove(value)
        return True
    except ValueError:
        return False
if __name__ == '__main__':
    data = [10, 20, 30, 40, 50]
    remove_by_index(data, 2)
    remove_by_value(data, 10)
    print(f"Updated list: {data}")