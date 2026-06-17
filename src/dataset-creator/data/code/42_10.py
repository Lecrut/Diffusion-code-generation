def sort_keys_alphabetically(keys):
    return sorted([key.lower() for key in keys])
if __name__ == '__main__':
    sample_data = ['Apple', 'banana', 'Cherry', 'date']
    sorted_result = sort_keys_alphabetically(sample_data)
    print(sorted_result)