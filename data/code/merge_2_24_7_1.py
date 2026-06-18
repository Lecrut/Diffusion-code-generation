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
    large_dataset = {
        "alpha": [10, 20, 30],
        "beta": ["a", "b"],
        "gamma": 42.5,
        "delta": {"nested": True},
        "epsilon": list(range(100))
    }
    start_time = time.time()
    for item in yield_from_dict(large_dataset):
        print(item)
    end_time = time.time()
    print(f"Execution completed in {end_time - start_time:.4f} seconds")