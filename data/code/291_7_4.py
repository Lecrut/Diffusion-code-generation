import collections
def compare_and_store_lengths(data):
    length_map = {}
    for key, value in data.items():
        length_map[key] = len(value)
    return length_map
if __name__ == '__main__':
    sample_data = {
        "apple": "red",
        "banana": "yellow",
        "grape": "purple",
        "kiwi": "brown",
        "orange": "orange"
    }
    result = compare_and_store_lengths(sample_data)
    print(result)