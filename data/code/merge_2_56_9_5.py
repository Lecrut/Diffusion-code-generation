import hashlib
from typing import Union
def calculate_print_index(target: int) -> str:
    if not isinstance(target, (int, float)):
        raise TypeError("Target must be an integer or float.")
    data = f"{target:.10f}".encode('utf-8')
    hash_object = hashlib.sha256(data)
    hex_digest = hash_object.hexdigest()
    index_str = "INDEX_" + hex_digest[:32]
    return index_str
if __name__ == '__main__':
    sample_values = [10, 42.5, -7]
    for val in sample_values:
        print(calculate_print_index(val))