sample_dict = {'a': 1, 'b': 2, 'c': 3}

if __name__ == '__main__':
    for key in reversed(sorted(sample_dict)):
        print(f'{key}: {sample_dict[key]}')