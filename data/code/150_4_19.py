BLACKLIST = "example"

def remove_blacklist_item(input_list):
    return [item for item in input_list if item != BLACKLIST]

if __name__ == '__main__':
    sample_list = ["apple", "banana", "cherry", "example"]
    filtered_list = remove_blacklist_item(sample_list)
    print(filtered_list)