def tuples_to_dict(store_ages):
    return dict(store_ages)

if __name__ == '__main__':
    sample_data = [('Store A', 30), ('Store B', 25), ('Store C', 40)]
    result = tuples_to_dict(sample_data)
    print(result)