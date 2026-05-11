def create_and_print_list():
    sample_data = [
        "apple",
        42,
        "banana",
        99,
        "cherry",
        101,
        "date",
        55,
        "elderberry",
        200
    ]
    print("Dynamically created list:")
    for index, item in enumerate(sample_data):
        print(f"{index + 1}. {item}")
if __name__ == '__main__':
    create_and_print_list()