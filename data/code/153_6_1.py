import sys
if __name__ == '__main__':
    list_data = ["apple", "banana", "cherry", "date"]
    if len(sys.argv) > 1:
        target_item = sys.argv[1]
        if target_item in list_data:
            print(f"'{target_item}' found in the list.")
        else:
            print(f"'{target_item}' not found in the list.")
    else:
        print("Please provide an item to check.")