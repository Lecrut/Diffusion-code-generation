def get_last_item(lst):
    if not lst:
        raise IndexError("The list is empty.")
    return lst[-1]

if __name__ == '__main__':
    sample_lists = {
        "fruits": ["apple", "banana", "cherry", "date"],
        "colors": ["red", "green", "blue"],
        "empty": []
    }
    
    for name, lst in sample_lists.items():
        try:
            last_item = get_last_item(lst)
            print(f"The list '{name}' is: {lst}")
            print(f"The last item in the list '{name}' is: {last_item}")
        except IndexError as e:
            print(e)