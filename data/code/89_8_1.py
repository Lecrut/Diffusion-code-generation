import operator
def evaluate_sequence(data, operations):
    if len(data) < 2:
        raise ValueError("Data must contain at least two elements")
    current_data = list(data[:])
    if not operations:
        return current_data
    for op_func in operations:
        if len(current_data) < 2:
            raise ValueError("Not enough elements to perform the operation")
        left = current_data.pop(0)
        right = current_data.pop(0)
        try:
            result = op_func(left, right)
            current_data.insert(0, result)
        except Exception as e:
            raise TypeError(f"Error during operation: {e}")
    return current_data
if __name__ == '__main__':
    numbers = [10, 20, 5, 3]
    operations = [operator.add, operator.sub, operator.mul]
    try:
        result = evaluate_sequence(numbers, operations)
        print(result)
    except Exception as e:
        print(f"An error occurred: {e}")