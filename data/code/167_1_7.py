def tuples_to_dict(store_age_list):
    return dict(store_age_list)

if __name__ == '__main__':
    sample_data = [('StoreA', 30), ('StoreB', 45), ('StoreC', 28)]
    result = tuples_to_dict(sample_data)
    print(result)