def find_maximum(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    maximum = data[0]
    for number in data[1:]:
        if number > maximum:
            maximum = number
    return maximum

if __name__ == '__main__':
    sample_lists = [
        [3, 1, 4, 1, 5, 9, 2],
        [-10, -5, -20, -1],
        [42],
        [100, 50, 25]
    ]
    
    for sample_list in sample_lists:
        print(f"The maximum of {sample_list} is: {find_maximum(sample_list)}")