def get_sorted_keys(data):
    keys = list(data.keys())
    keys.sort()
    return keys
if __name__ == '__main__':
    sample_dict = {
        "apple": "fruit",
        "zebra": "animal",
        "banana": "fruit",
        "cat": "mammal"
    }
    result = get_sorted_keys(sample_dict)
    print(result)