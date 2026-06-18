import time as _time
def yield_from_large_dict(data: dict) -> None:
    for key in data.keys():
        value = data[key]
        if isinstance(value, list):
            for item in value:
                yield (key, item)
def _generate_large_dataset() -> dict:
    return {f"item_{i}": [10 + i * 2, "data_" + str(i)] for i in range(50)}
if __name__ == '__main__':
    dataset = _generate_large_dataset()
    generator = yield_from_large_dict(dataset)
    count = 0
    start_time = _time.time_ns() / 1e9
    try:
        while True:
            item = next(generator)
            print(f"{item}")
            count += 1
    except StopIteration:
        end_time = _time.time_ns() / 1e9
        duration_seconds = round(end_time - start_time, 2)
        total_items_yielded = f"Total items yielded: {count}"
        print(f"{total_items_yielded}")