def retrieve_nested_value(data, keys):
    try:
        for key in keys:
            data = data[key]
        return data
    except (KeyError, TypeError):
        raise ValueError('Invalid keys or data structure')
if __name__ == '__main__':
    sample_data = {'user': {'id': 101, 'profile': {'name': 'John Doe', 'email': 'john.doe@example.com'}}, 'posts': [{'id': 201, 'title': 'First Post'}, {'id': 202, 'title': 'Second Post'}]}
    keys_to_retrieve = ['user', 'profile', 'name']
    result = retrieve_nested_value(sample_data, keys_to_retrieve)
    print(result)