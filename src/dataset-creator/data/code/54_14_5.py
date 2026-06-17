import math
def find_middle_position(items):
    if not isinstance(items, (list, tuple)):
        raise TypeError("Input must be a list or tuple.")
    length = len(items)
    if length == 0:
        return None
    mid_index = math.floor(length / 2)
    return mid_index
if __name__ == '__main__':
    sample_data = [1, 5, 3, 9, 7]
    try:
        middle_pos = find_middle_position(sample_data)
        print(f"Middle position index: {middle_pos}")
        if middle_pos is not None:
            value_at_mid = sample_data[middle_pos]
            print(f"Value at middle position: {value_at_mid}")
    except Exception as e:
        print(f"Error occurred: {e}")