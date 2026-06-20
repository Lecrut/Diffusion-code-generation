def has_required_keys(data):
    return all((key in data and data[key] is not None for key in ('id', 'name', 'status')))
if __name__ == '__main__':
    sample_data = {'id': 123, 'name': 'Example', 'status': 'active'}
    print(has_required_keys(sample_data))