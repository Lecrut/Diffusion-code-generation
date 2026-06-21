import bisect

def insert_item(sorted_items, item_name):
    bisect.insort(sorted_items, item_name)

def search_item(sorted_items, item_name):
    index = bisect.bisect_left(sorted_items, item_name)
    if index != len(sorted_items) and sorted_items[index] == item_name:
        return True
    return False

if __name__ == '__main__':
    sample_items = ["Apple", "Banana", "Cherry"]
    new_item = "Orange"

    insert_item(sample_items, new_item)
    print(f"Inserted: {sample_items}")

    search_query = "Banana"
    if search_item(sample_items, search_query):
        print(f"'{search_query}' found in the list.")
    else:
        print(f"'{search_query}' not found in the list.")

    search_query = "Grape"
    if search_item(sample_items, search_query):
        print(f"'{search_query}' found in the list.")
    else:
        print(f"'{search_query}' not found in the list.")