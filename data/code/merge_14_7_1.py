def process_file():
    data = {
        "apple": "red",
        "banana": "yellow",
        "carrot": "orange",
        "grape": "purple"
    }
    print("--- Item Dictionary ---")
    for item, color in data.items():
        print(f"{item}: {color}")
if __name__ == '__main__':
    process_file()