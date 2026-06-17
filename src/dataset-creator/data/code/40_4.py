def contains_key(mapping: dict, target: str) -> bool:
    return target in mapping
if __name__ == '__main__':
    data = {'apple': 10, 'banana': 20}
    print(contains_key(data, 'orange'))