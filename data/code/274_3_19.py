def print_nested_list(nested_list):
    def recursive_print(sub_list):
        for item in sub_list:
            if isinstance(item, list):
                recursive_print(item)
            else:
                print(item)

    recursive_print(nested_list)

if __name__ == '__main__':
    sample = [1, [2, 3], [4, [5, 6]], 7]
    try:
        print_nested_list(sample)
    except Exception as e:
        print(f"An error occurred: {e}")