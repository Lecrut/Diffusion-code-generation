def get_last_element(lst):
    return lst[-1]

if __name__ == '__main__':
    sample_list = ["apple", "banana", "cherry", "date"]
    last_item = get_last_element(sample_list)
    print(f"List: {sample_list}")
    print(f"Last item: {last_item}")