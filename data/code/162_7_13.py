MAX_NAME_LENGTH = 20

def name_length_mapping(user_names):
    return {name: len(name) if len(name) <= MAX_NAME_LENGTH else MAX_NAME_LENGTH for name in user_names}

if __name__ == '__main__':
    sample_user_names = ['Alice', 'Bob', 'Charlie', 'David']
    result = name_length_mapping(sample_user_names)
    print(result)