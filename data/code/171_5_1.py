import uuid
def generate_unique_store_id(prefix: str, sequence_number: int) -> str:
    unique_part = str(uuid.uuid4().int)[:8]
    store_id = f"{prefix}-{sequence_number}-{unique_part}"
    return store_id
if __name__ == '__main__':
    prefix = "STORE"
    sequence = 101
    store_id1 = generate_unique_store_id(prefix, sequence)
    print(f"Generated Store ID 1: {store_id1}")
    sequence = 102
    store_id2 = generate_unique_store_id(prefix, sequence)
    print(f"Generated Store ID 2: {store_id2}")
    sequence = 999
    store_id3 = generate_unique_store_id(prefix, sequence)
    print(f"Generated Store ID 3: {store_id3}")