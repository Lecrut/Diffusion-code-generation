def tuples_to_dict(store_tuples):
    return dict(store_tuples)

if __name__ == '__main__':
    sample_data = [('Store A', 25), ('Store B', 30), ('Store C', 35)]
    result = tuples_to_dict(sample_data)
    print(result)