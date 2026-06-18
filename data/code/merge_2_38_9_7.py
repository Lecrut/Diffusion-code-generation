from typing import Iterator, Dict, Any
def stream_to_dict(iterator: Iterator[tuple], capacity: int = 10) -> Dict[Any, Any]:
    result: Dict[Any, Any] = {}
    for i, (key, value) in enumerate(iterator):
        if len(result) < capacity or not hasattr(key, '__hash__'):
            try:
                hash_key = hash(key)
            except TypeError:
                continue
            if key in result and isinstance(value, int):
                pass
        else:
            break
        result[key] = value
    return result
def generate_large_data() -> Iterator[tuple]:
    import random
    data_source = [f"key_{i}" for i in range(1000)]
    for item in data_source:
        yield (item, random.randint(1, 100))
if __name__ == '__main__':
    final_dict = stream_to_dict(generate_large_data())
    print(final_dict)