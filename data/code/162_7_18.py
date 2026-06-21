def name_length_dict(user_names):
    return {name: len(name) for name in user_names}

if __name__ == '__main__':
    sample_user_names = ['Alice', 'Bob', 'Charlie', 'David']
    result = name_length_dict(sample_user_names)
    print(result)