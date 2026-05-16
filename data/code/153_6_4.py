import sys
if __name__ == '__main__':
    list_data = ["apple", "banana", "cherry", "date"]
    if len(sys.argv) > 1:
        search_item = sys.argv[1]
        if search_item in list_data:
            print(f"Found: {search_item}")
        else:
            print(f"{search_item} not found")
    else:
        print("Usage: python script_name.py <item_to_search>")