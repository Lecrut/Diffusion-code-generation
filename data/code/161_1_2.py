def create_item_list(string_list):
    return sorted(string_list)
if __name__ == '__main__':
    sample_list = ["banana", "apple", "cherry", "date"]
    sorted_list = create_item_list(sample_list)
    print(sorted_list)