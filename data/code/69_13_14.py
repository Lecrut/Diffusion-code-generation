def retrieve_nested_value(data, keys):
    for key in keys:
        if isinstance(data, dict) and key in data:
            data = data[key]
        else:
            return None
    return data
if __name__ == '__main__':
    sample_data = {'user': {'id': 101, 'profile': {'name': 'John Doe', 'email': 'john.doe@example.com'}}, 'posts': [{'id': 1, 'content': 'Hello World'}, {'id': 2, 'content': 'Python is great!'}]}
    keys_to_retrieve = ['user', 'profile', 'name']
    result = retrieve_nested_value(sample_data, keys_to_retrieve)
    print(result)