import sys
if __name__ == '__main__':
    items_from_stdin = ["apple", "banana", "cherry", "date"]
    if len(sys.argv) < 2:
        print("Usage: python script_name.py <item_to_check>")
    else:
        item_to_check = sys.argv[1]
        found = item_to_check in items_from_stdin
        if found:
            print(f"{item_to_check}: Found in the list.")
        else:
            print(f"{item_to_check}: Not found in the list.")