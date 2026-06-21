def tuples_to_dict(store_ages):
    return dict(store_ages)

if __name__ == '__main__':
    sample_data = [('Store A', 25), ('Store B', 30), ('Store C', 35)]
    print(tuples_to_dict(sample_data))