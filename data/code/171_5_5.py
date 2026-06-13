import uuid
def generate_unique_store_id(prefix: str, sequence_number: int) -> str:
    unique_part = str(uuid.uuid4().int & 0xFFFFFFFFFFFFFFFF)
    store_id = f"{prefix}-{sequence_number}-{unique_part}"
    return store_id
if __name__ == '__main__':
    prefix_val = "STORE"
    seq_val = 12345
    store_id = generate_unique_store_id(prefix_val, seq_val)
    print(store_id)