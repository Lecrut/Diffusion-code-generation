def validate_input(arr):
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    if len(arr) == 0:
        raise ValueError("List cannot be empty")

def get_final_item(arr):
    validate_input(arr)
    return arr[-1]

if __name__ == '__main__':
    sample_list = [7, 8, 9, 10]
    print(get_final_item(sample_list))