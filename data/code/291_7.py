import collections
def optimize_string_lengths(data):
    length_map = {}
    for key, value in data.items():
        length_map[key] = len(value)
    return length_map
if __name__ == '__main__':
    sample_data = {
        "apple": "app",
        "banana": "bananas",
        "kiwi": "kiwi",
        "orange": "orange",
        "grape": "grapefruit"
    }
    result = optimize_string_lengths(sample_data)
    print(result)