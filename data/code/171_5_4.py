import uuid
def generate_unique_store_id(prefix: str, sequence_number: int) -> str:
    unique_part = str(uuid.uuid4().int)[:8]
    store_id = f"{prefix}-{sequence_number}-{unique_part}"
    return store_id
if __name__ == '__main__':
    prefix = "STORE"
    sequence = 12345
    store_id = generate_unique_store_id(prefix, sequence)
    print(store_id)