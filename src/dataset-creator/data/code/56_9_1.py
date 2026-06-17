import hashlib
def calculate_print_index(target: int) -> str:
    data = f"{target}".encode('utf-8')
    digest = hashlib.sha256(data).hexdigest()
    return digest[:10]
if __name__ == '__main__':
    sample_values = [42, 9753, -100, 0]
    for val in sample_values:
        print(f"Target {val}: Index is {calculate_print_index(val)}")