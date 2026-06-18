def delete_entry(data_structure, key_or_value):
    if isinstance(data_structure, dict) and key_or_value in data_structure:
        del data_structure[key_or_value]
    elif isinstance(data_structure, list) and key_or_value in data_structure:
        data_structure.remove(key_or_value)
if __name__ == '__main__':
    sample_dict = {'apple': 5, 'banana': 3}
    sample_list = [10, 20, 30]
    delete_entry(sample_dict, 'orange')
    print("Dict after missing key deletion:", sample_dict)
    delete_entry(sample_dict, 'apple')
    print("Dict after successful key deletion:", sample_dict)
    delete_entry(sample_list, 5)
    print("List after missing value removal:", sample_list)
    delete_entry(sample_list, 20)
    print("List after successful value removal:", sample_list)