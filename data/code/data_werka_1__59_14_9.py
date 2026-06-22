def validate_input(data):
    if not isinstance(data, list):
        raise ValueError("Input must be a list.")
    if len(data) == 0:
        raise ValueError("List cannot be empty.")

def find_middle(data):
    validate_input(data)
    middle_index = len(data) // 2
    return data[middle_index]

if __name__ == '__main__':
    sample_lists = [
        [1, 2, 3, 4, 5],
        [10, 20, 30, 40],
        [50],
        [100, 200]
    ]
    
    for lst in sample_lists:
        print(find_middle(lst))