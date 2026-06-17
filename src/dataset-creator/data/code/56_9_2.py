import hashlib
from typing import Any, Union
def calculate_print_index(target: Union[int, str], salt: bytes) -> int:
    if isinstance(salt, str):
        raise TypeError("Salt must be provided as bytes.")
    combined = f"{target}:{salt.decode('utf-8')}".encode('utf-8')
    hash_obj = hashlib.sha256(combined)
    hex_digest = hash_obj.hexdigest()
    index_value = int(hex_digest[:16], 16) % (0x7FFFFFFF + 1)
    return index_value
if __name__ == '__main__':
    sample_target: str = "production_ready_index"
    sample_salt: bytes = b"secure_secret_key_2024"
    result_index = calculate_print_index(sample_target, sample_salt)
    print(f"Print Index for '{sample_target}': {result_index}")