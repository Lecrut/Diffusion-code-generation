def insert_element(data_list: list, new_value: int, index: int) -> bool:
    try:
        data_list.insert(index, new_value)
        return True
    except IndexError:
        return False

def main():
    initial_list = [10, 20, 30, 40]
    new_value = 25
    valid_index = 2
    invalid_index = 100

    result = initial_