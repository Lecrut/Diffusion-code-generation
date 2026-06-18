def process_file():
    data = {
        "apple": 1,
        "banana": 2,
        "cherry": 3,
        "date": 4
    }
    print("--- Item Dictionary ---")
    for item, value in data.items():
        print(f"{item}: {value}")
if __name__ == '__main__':
    process_file()