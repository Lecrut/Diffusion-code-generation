def initialize_data():
    data = {}
    for i in range(10):
        key = f"int_{i}"
        value = (i ** 2) * 3 + 7
    words = ["apple", "banana", "cherry"]
    data["word_list"] = tuple(words)
    return data
if __name__ == '__main__':
    result_dict = initialize_data()