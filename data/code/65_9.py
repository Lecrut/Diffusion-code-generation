def find_and_retrieve(data_list, position):
    if 0 <= position < len(data_list):
        return data_list[position]
    else:
        raise IndexError("Position out of bounds")
if __name__ == '__main__':
    my_list = [10, 20, 30, 40, 50]
    target_position = 2
    try:
        result = find_and_retrieve(my_list, target_position)
        print(result)
    except IndexError as e:
        print(f"Error: {e}")