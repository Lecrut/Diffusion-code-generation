import uuid
def generate_unique_store_id(prefix: str, sequence: int) -> str:
    unique_part = str(uuid.uuid4().int)[:8]
    store_id = f"{prefix}-{sequence}-{unique_part}"
    return store_id
if __name__ == '__main__':
    prefix_val = "STORE"
    sequence_val = 101
    store_id_1 = generate_unique_store_id(prefix_val, sequence_val)
    print(f"Generated Store ID 1: {store_id_1}")
    prefix_val = "BRANCH"
    sequence_val = 5
    store_id_2 = generate_unique_store_id(prefix_val, sequence_val)
    print(f"Generated Store ID 2: {store_id_2}")