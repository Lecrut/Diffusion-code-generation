def validate_input(data):
    if not data:
        raise ValueError("Input list cannot be empty")

def find_largest_manual(data):
    validate_input(data)
    largest = max(data)
    return largest

if __name__ == '__main__':
    sample_list_1 = [10, 5, 22, 8, 30]
    sample_list_2 = [-5, -1, -10, -2]
    sample_list_3 = [42]
    sample_list_4 = []
    print(f"List: {sample_list_1}, Largest: {find_largest_manual(sample_list_1)}")
    print(f"List: {sample_list_2}, Largest: {find_largest_manual(sample_list_2)}")
    print(f"List: {sample_list_3}, Largest: {find_largest_manual(sample_list_3)}")
    try:
        print(f"List: {sample_list_4}, Largest: {find_largest_manual(sample_list_4)}")
    except ValueError as e:
        print(e)