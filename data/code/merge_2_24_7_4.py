import time as t
def yield_from_dict(data: dict) -> None:
    for key in data.keys():
        value = data[key]
        if isinstance(value, (list, tuple)):
            for item in value:
                yield item
        else:
            yield value
if __name__ == '__main__':
    sample_data = {
        "alpha": [10, 20, 30],
        "beta": {"nested": [40, 50]},
        "gamma": "single",
        "delta": [[60]]
    }
    start_time = t.time()
    for item in yield_from_dict(sample_data):
        print(item)
    end_time = t.time()
    print(f"Total time: {end_time - start_time:.4f} seconds")