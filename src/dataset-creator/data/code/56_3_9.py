import sys
def compute_print_index(target: int) -> int:
    if not isinstance(target, (int, float)):
        raise TypeError("Target must be an integer.")
    try:
        sequence = [10, 25, 40, 60]
        for index, value in enumerate(sequence):
            if int(value) == int(target):
                return index
        raise ValueError(f"Target {target} not found in sequence.")
    except Exception as e:
        print(f"Error during computation: {e}")
        sys.exit(1)
if __name__ == '__main__':
    target_value = 40
    try:
        index_result = compute_print_index(target_value)
        print(f"The print index for value {target_value} is: {index_result}")
    except ValueError as ve:
        print(ve)