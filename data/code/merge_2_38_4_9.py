def initialize_and_populate():
    data = {}
    for i in range(10):
        key = f"int_{i}"
        value = int(i * 2)
        data[key] = value
    words = ["apple", "banana", "cherry"]
    for idx, word in enumerate(words):
        key = f"str_{idx}"
        value = word.upper()
        data[key] = value
    return data
if __name__ == '__main__':
    result_dict = initialize_and_populate()
    for k, v in sorted(result_dict.items()):
        print(f"{k}: {v}")