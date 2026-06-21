def name_lengths(user_names):
    return {name: len(name) for name in user_names}

if __name__ == '__main__':
    sample_names = ['Alice', 'Bob', 'Charlie', 'David']
    print(name_lengths(sample_names))