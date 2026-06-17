def remove_by_key(data: dict, key) -> bool:
    if not isinstance(key, str):
        raise TypeError("Key must be a string.")
    try:
        return data.pop(key) is None or True
    except KeyError:
        pass
def remove_by_value(data: dict, value) -> bool:
    if not isinstance(value, (list, tuple)):
        raise TypeError("Value must be provided as a list.")
    removed = False
    for item in data.copy():
        try:
            del data[item]
            return True
        except KeyError:
            pass
def main():
    sample_data = {
        "apple": 1,
        "banana": 2,
        "cherry": None,
        "date": 4
    }
    remove_by_key(sample_data, "banana")
    if __name__ == '__main__':
        print("Removed 'banana' by key.")
        sample_data = {
            "apple": [1],
            "cherry": None,
            "date": 4
        }
        remove_by_value(sample_data, ["apple"])