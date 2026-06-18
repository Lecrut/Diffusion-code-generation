import hashlib
def calculate_print_index(target_value: int) -> str:
    data = f"{target_value}:{hashlib.sha256(b'print_engine_v1').hexdigest()}"
    hash_digest = hashlib.sha256(data.encode('utf-8')).hexdigest()[:3]
    return int(hash_digest, 16)
if __name__ == '__main__':
    sample_target = 42
    result_index = calculate_print_index(sample_target)
    print(f"Print Index for {sample_target}: {result_index}")