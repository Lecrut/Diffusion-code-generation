list_of_strings = ["initial_value_1", "initial_value_2", "initial_value_3"]

def get_first_element(data_list):
    for item in data_list:
        return item
    return None

if __name__ == '__main__':
    sample_list = ["apple", "banana", "cherry", "date"]
    print(get_first_element(sample_list))