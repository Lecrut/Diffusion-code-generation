def initialize_data():
    data = {}
    for i in range(10):
        key = f"int_{i}"
        value = 2 ** i
        data[key] = value
    words = ["apple", "banana", "cherry"]
    for idx, word in enumerate(words):
        key = f"str_word_{idx}"
        value = len(word) * ord("a") + 100
        data[key] = str(value).zfill(4)
    return data
if __name__ == '__main__':
    result_dict = initialize_data()