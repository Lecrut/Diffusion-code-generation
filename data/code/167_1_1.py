def list_to_dict(tuples_list):
    return dict(tuples_list)

if __name__ == '__main__':
    sample_data = [('Store A', 30), ('Store B', 25), ('Store C', 40)]
    result = list_to_dict(sample_data)
    print(result)