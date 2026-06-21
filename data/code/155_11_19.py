def validate_input(data):
    if not all(isinstance(x, int) for x in data):
        raise ValueError("All elements must be integers.")
    if len(data) == 0:
        raise ValueError("List cannot be empty.")

def calculate_sum(data):
    return sum(data)

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    validate_input(sample_list)
    result = calculate_sum(sample_list)
    print(result)