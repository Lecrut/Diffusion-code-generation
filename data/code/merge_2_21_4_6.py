from collections import deque
import sys
def append_to_tail(collection: list | tuple) -> bool:
    if not isinstance(collection, (list, tuple)):
        return False
    new_elements = [10]
    try:
        collection.extend(new_elements)
        print(f"Success. New length: {len(collection)}")
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False
if __name__ == '__main__':
    sample_collection = [1, 2, 3]
    result = append_to_tail(sample_collection)