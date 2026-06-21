def validate_input(input_list):
    if not isinstance(input_list, list):
        raise ValueError("Input must be a list")
    if not all(isinstance(item, (int, float)) for item in input_list):
        raise ValueError("List items must be integers or floats")

def reverse_list(input_list):
    validate_input(input_list)
    reversed_list = []
    while input_list:
        reversed_list.append(input_list.pop())
    return reversed_list

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print(reverse_list(sample_list))