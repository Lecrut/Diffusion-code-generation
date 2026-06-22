from typing import List, TypeVar, Any

T = TypeVar('T')

INDEX_OFFSET = 1

def get_last_item(collection: List[T]) -> T:
    total_length = len(collection)
    target_index = total_length - INDEX_OFFSET
    return collection[target_index]

if __name__ == '__main__':
    test_data = [100, 200, 300, 400, 500]
    output_value = get_last_item(test_data)
    print(output_value)