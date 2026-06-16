import time
def yield_from_dict(data):
    for key in data:
        value = data[key]
        if isinstance(value, (list, tuple)):
            for item in value:
                yield f"{key}: {item}"
        else:
            yield f"{key}: {value}"
if __name__ == '__main__':
    sample_data = {
        "fruits": ["apple", "banana", "cherry"],
        "numbers": [1, 2, 3],
        "single_item": "end"
    }
    generator = yield_from_dict(sample_data)
    start_time = time.time()
    for item in generator:
        print(item)
    end_time = time.time()
    print(f"\nTotal execution time (yield loop): {end_time - start_time:.4f} seconds")