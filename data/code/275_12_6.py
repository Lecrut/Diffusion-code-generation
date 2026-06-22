FLATTENED_ITEM_INDENT = "  "

def flatten_and_print(nested_list):
    def recursive_flatten(sublist, indent_level=0):
        for item in sublist:
            if isinstance(item, list):
                recursive_flatten(item, indent_level + 1)
            else:
                print(indent_level * FLATTENED_ITEM_INDENT + str(item))
    
    recursive_flatten(nested_list)

if __name__ == '__main__':
    sample_data = [1, [2, 3], [4, [5, 6]], 7]
    flatten_and_print(sample_data)