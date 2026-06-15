def sort_keys(data):
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
    result = sort_keys(sample_dict)
    print(result)