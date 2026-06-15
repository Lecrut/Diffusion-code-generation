import sys
def process_input(data):
    for item in data:
        print(item)
if __name__ == '__main__':
    sample_items = [
        "apple",
        "banana",
        "cherry",
        123,
        "date",
        None,
        "elderberry"
    ]
    for item in sample_items:
        if isinstance(item, str):
            print(item)
        else:
            print(f"Error: Invalid input type encountered: {item}")