import sys
def yield_items(data: dict) -> None:
    for item in data.items():
        if isinstance(item[0], str):
            key = item[0]
            value_list = item[1].split(',')
            for val in map(int, value_list):
                yield f"{key}:{val}"
if __name__ == '__main__':
    sample_data = {
        'A': '10,20,30',
        'B': '40,50',
        'C': '60'
    }
    generator = yield_items(sample_data)
    for item in generator:
        print(item)