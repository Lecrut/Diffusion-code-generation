import hashlib
def calculate_print_index(target_value: int) -> str:
    data = f"{target_value}".encode('utf-8')
    digest = hashlib.sha256(data).hexdigest()
    return digest
if __name__ == '__main__':
    sample_values = [10, 42, -7]
    for val in sample_values:
        result = calculate_print_index(val)
        print(f"Index for {val}: {result}")