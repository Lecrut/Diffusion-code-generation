import bisect

def find_item(sorted_items, item_name):
    index = bisect.bisect_left(sorted_items, item_name)
    if index != len(sorted_items) and sorted_items[index] == item_name:
        return True
    return False

def insert_item(sorted_items, item_name):
    bisect.insort_left(sorted_items, item_name)

if __name__ == '__main__':
    sample_items = ['Apple', 'Banana', 'Cherry']
    item_to_find = "Banana"
    item_to_insert = "Date"

    print(f"Finding '{item_to_find}' in the list: {find_item(sample_items, item_to_find)}")
    insert_item(sample_items, item_to_insert)
    print("Updated list after insertion:", sample_items)