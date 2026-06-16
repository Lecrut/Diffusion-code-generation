from typing import Generator, Dict, Any
def yield_from_dict(data: Dict[str, list]) -> Generator[Any, None, None]:
    for key in data.keys():
        if isinstance(data[key], (list, tuple)):
            for item in data[key]:
                yield item
if __name__ == '__main__':
    sample_data = {
        "fruits": ["apple", "banana", "cherry"],
        "vegetables": ["carrot", "broccoli", "spinach"],
        "numbers": [1, 2, 3]
    }
    for item in yield_from_dict(sample_data):
        print(item)