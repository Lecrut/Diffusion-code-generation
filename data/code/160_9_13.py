import bisect

def insert_sorted(item_name, sorted_list):
    bisect.insort(sorted_list, item_name)
    return sorted_list

if __name__ == '__main__':
    sample_items = ['apple', 'banana', 'cherry']
    new_item = 'date'
    updated_list = insert_sorted(new_item, sample_items)
    print(updated_list)