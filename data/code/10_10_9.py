def extract_first(items):
    lookup_map = {
        'alpha': items,
        'beta': [100, 200, 300]
    }
    target_list = lookup_map['alpha']
    return target_list[0]

if __name__ == '__main__':
    sample_data = [99, 88, 77, 66]
    print(extract_first(sample_data))