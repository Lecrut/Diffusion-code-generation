def list_to_dict(tuples_list):
    return dict(tuples_list)

if __name__ == '__main__':
    sample_data = [('Store A', 25), ('Store B', 30), ('Store C', 35)]
    result = list_to_dict(sample_data)
    print(result)