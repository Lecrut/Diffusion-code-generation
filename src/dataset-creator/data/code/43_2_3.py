import json
def delete_entry(data: dict, key_or_value) -> bool:
    if not isinstance(key_or_value, (str, int)):
        return False
    try:
        del data[key_or_value]
        return True
    except KeyError:
        pass
    for k in list(data.keys()):
        if data[k] == key_or_value:
            del data[k]
            return True
    return False
if __name__ == '__main__':
    sample_data = {"apple": 1, "banana": 2, "cherry": 3}
    delete_entry(sample_data, 2)
    print("After deleting value 2:", json.dumps(sample_data))
    sample_data["date"] = 4
    delete_entry(sample_data, "banana")                                      
    print("After trying to delete non-existent entry:", json.dumps(sample_data))