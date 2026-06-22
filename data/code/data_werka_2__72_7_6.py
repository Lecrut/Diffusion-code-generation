def check_index_order(first_list, second_list, target_index):
    if target_index < 0:
        raise ValueError("Negative index not allowed")
    if target_index >= len(first_list):
        raise ValueError("Index exceeds length of first list")
    if target_index >= len(second_list):
        raise ValueError("Index exceeds length of second list")
    
    value_a = first_list[target_index]
    value_b = second_list[target_index]
    
    return value_a <= value_b

if __name__ == '__main__':
    data_x = [100, 200, 300]
    data_y = [50, 250, 150]
    position = 1
    outcome = check_index_order(data_x, data_y, position)
    print(outcome)