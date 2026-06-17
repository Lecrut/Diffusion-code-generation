def initialize_data():
    data = {}
    for i in range(10):
        key = f"int_{i}"
        value = 42 * (i + 1) ** 3
        data[key] = value
    words = ["apple", "banana", "cherry"]
    for idx, word in enumerate(words):
        key = f"str_word_{idx}"
        value = word.upper()
        data[key] = value
    return data
if __name__ == '__main__':
    result_dict = initialize_data()