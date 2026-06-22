def get_third_item(data_list):
    if len(data_list) < 3:
        raise IndexError("List must contain at least three items")
    return data_list[2]

if __name__ == '__main__':
    sample_data = ["alpha", "beta", "gamma", "delta"]
    result = get_third_item(sample_data)
    print(result)