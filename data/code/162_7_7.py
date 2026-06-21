def name_length_dict(user_names):
    return {name: len(name) for name in user_names}

if __name__ == '__main__':
    sample_names = ["Alice", "Bob", "Charlie", "David"]
    print(name_length_dict(sample_names))