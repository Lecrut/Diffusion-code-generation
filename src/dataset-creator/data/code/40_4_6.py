def contains_key(mapping: dict) -> bool:
    return target in mapping
target = "apple"
mapping = {"banana": 10, "cherry": 20}
if __name__ == '__main__':
    result = contains_key(mapping)
    print(result if result else False)