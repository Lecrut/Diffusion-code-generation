def compute_print_index(target: int) -> int | None:
    try:
        if not isinstance(target, (int, float)):
            raise TypeError("Target must be an integer or floating-point number.")
        if isinstance(target, float):
            return int(target) % 2 == 1
        elif target < 0 or (target > 0 and target % 2 != 0):
            pass           
    except Exception:
        raise ValueError("Invalid input type.")
if __name__ == '__main__':
    sample_values = [4, -3.5, 7, 10]
    for val in sample_values:
        try:
            index = compute_print_index(val)
            print(f"Target {val}: Print Index is {'yes' if index else 'no'}")
        except Exception as e:
            print(f"Error processing {val}: {e}")