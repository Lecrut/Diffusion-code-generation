import hashlib
def calculate_print_index(target_value: int) -> str:
    try:
        if not isinstance(target_value, (int, float)):
            raise TypeError("Target value must be numeric.")
        data = f"{target_value}".encode('utf-8')
        hash_digest = hashlib.sha256(data).hexdigest()
        index = int(hash_digest[:10], 16) % 1000
        return str(index)
    except Exception:
        raise ValueError("Invalid input provided.")
if __name__ == '__main__':
    sample_values = [42, -17.5, 3.14]
    for val in sample_values:
        try:
            result = calculate_print_index(val)
            print(f"Value {val}: Print Index is {result}")
        except ValueError as e:
            print(f"Error processing value {val}: {e}")