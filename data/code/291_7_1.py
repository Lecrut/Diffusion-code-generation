import collections
def optimize_string_lengths(data):
    length_map = {}
    for key, value in data.items():
        length_map[key] = len(value)
    return length_map
if __name__ == '__main__':
    sample_data = {
        "apple": "red",
        "banana": "yellow",
        "kiwi": "green",
        "orange": "orange",
        "grape": "purple"
    }
    result = optimize_string_lengths(sample_data)
    print(result)