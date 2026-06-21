def access_list_elements(data_list, indices):
    try:
        return [data_list[index] for index in indices if 0 <= index < len(data_list)]
    except IndexError as e:
        print(f"IndexError: {e}")
        return []

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    indices_to_access = [1, 3, 5, -1]
    result = access_list_elements(sample_list, indices_to_access)
    print(result)