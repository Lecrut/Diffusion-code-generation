import hashlib
def calculate_print_index(target: int) -> str:
    if not isinstance(target, (int, float)):
        raise TypeError("Target must be an integer or float.")
    data = f"{target}".encode('utf-8')
    digest = hashlib.sha256(data).hexdigest()
    index_hash = int(digest[:10], 16) % 10
    return str(index_hash)
if __name__ == '__main__':
    sample_values = [42, -3.14, 987]
    for val in sample_values:
        print(f"Target {val}: Print Index {calculate_print_index(val)}")