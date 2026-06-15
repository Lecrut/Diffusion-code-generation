import sys
def process_input(data):
    for item in data:
        print(item)
if __name__ == '__main__':
    sample_items = [
        "Apple",
        "Banana",
        "Cherry",
        123,
        "Date",
        None,
        "Elderberry"
    ]
    for item in sample_items:
        if isinstance(item, str):
            print(item)
        elif isinstance(item, int):
            print(str(item))
        else:
            print("Invalid input encountered.")