def sort_keys(keys):
    return sorted([key.lower() for key in keys])
if __name__ == '__main__':
    sample_data = ["Apple", "banana", "Cherry", "date", "Elderberry"]
    result = sort_keys(sample_data)
    print(result)