def sort_dictionary_values(data):
    values = list(data.values())
    values.sort()
    return values
if __name__ == '__main__':
    sample_data = {
        "apple": "red",
        "banana": "yellow",
        "grape": "purple",
        "orange": "orange"
    }
    sorted_words = sort_dictionary_values(sample_data)
    print(sorted_words)