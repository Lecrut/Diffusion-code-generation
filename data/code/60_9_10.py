def get_last_item(item_list):
    if not item_list:
        raise ValueError("The list is empty.")
    return item_list[-1]

if __name__ == '__main__':
    sample_lists = {
        "fruits": ["apple", "banana", "cherry", "date"],
        "vegetables": ["carrot", "broccoli", "spinach"],
        "empty": []
    }
    
    for list_name, items in sample_lists.items():
        try:
            last_item = get_last_item(items)
            print(f"The last item in the {list_name} list is: {last_item}")
        except ValueError as e:
            print(e)