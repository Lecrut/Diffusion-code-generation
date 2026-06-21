MAX_NAME_LENGTH = 10

def map_user_names_to_lengths(user_names):
    return {name: len(name) if len(name) <= MAX_NAME_LENGTH else MAX_NAME_LENGTH for name in user_names}

if __name__ == '__main__':
    sample_user_names = ['Alice', 'Bob', 'Charlie', 'David']
    result = map_user_names_to_lengths(sample_user_names)
    print(result)