def calculate_sum(values):
    if not all(isinstance(x, (int, float)) for x in values):
        raise ValueError("All elements must be integers or floats")
    
    return sum(values)

if __name__ == '__main__':
    my_list = [1, 5.5, 10, 2]
    print(calculate_sum(my_list))