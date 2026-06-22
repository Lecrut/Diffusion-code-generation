def compare_elements_greater(list_x, list_y):
    if not list_x or not list_y:
        return []
    
    limit = min(len(list_x), len(list_y))
    matches = []
    
    for idx in range(limit):
        if list_x[idx] > list_y[idx]:
            print(f"{list_x[idx]} > {list_y[idx]}")
            matches.append(list_x[idx])
            
    return matches

if __name__ == '__main__':
    data_left = [9, 12, 1, 7]
    data_right = [5, 10, 4, 8]
    valid_greater_values = compare_elements_greater(data_left, data_right)
    print(valid_greater_values)