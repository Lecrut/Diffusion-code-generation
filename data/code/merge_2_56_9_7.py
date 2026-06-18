import hashlib
from typing import Union
def calculate_print_index(target: int) -> str:
    if not isinstance(target, (int, float)):
        raise TypeError("Target must be an integer or float.")
    data = f"{target:.10f}"
    hash_obj = hashlib.sha256(data.encode('utf-8'))
    hex_digest = hash_obj.hexdigest()[:16]
    index_value = int(hex_digest, 16) % (2**32 - 1)
    return str(index_value)
if __name__ == '__main__':
    sample_values = [42, 0.5, -987, 1e-5]
    for val in sample_values:
        print(f"Target: {val} -> Print Index: {calculate_print_index(val)}")