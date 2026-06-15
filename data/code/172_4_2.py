def process_dictionary(data):
    keys = list(data.keys())
    keys.sort()
    return keys
if __name__ == '__main__':
    sample_data = {
        "apple": "fruit",
        "zebra": "animal",
        "banana": "fruit",
        "cat": "mammal"
    }
    result = process_dictionary(sample_data)
    print(result)