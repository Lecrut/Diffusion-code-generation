def find_the_middle_value_among_three_batch_process(values):
    if not all(isinstance(x, (int, float)) for x in values) or len(values) != 3:
        raise ValueError("Input must be a list of exactly three numbers.")
    
    sorted_values = sorted(values)
    return sorted_values[1]

if __name__ == '__main__':
    print(find_the_middle_value_among_three_batch_process([1, 5, 3]))
    print(find_the_middle_value_among_three_batch_process([10, 20, 5]))
    print(find_the_middle_value_among_three_batch_process([7, 1, 9]))
    print(find_the_middle_value_among_three_batch_process([4, 8, 2]))
    print(find_the_middle_value_among_three_batch_process([100, 50, 25]))