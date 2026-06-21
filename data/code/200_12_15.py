EXTRACTED_KEYS = {'name', 'email'}

def extract_required_keys(data):
    return list(map(lambda x: {k: v for k, v in x.items() if k in EXTRACTED_KEYS}, data))

if __name__ == '__main__':
    sample_data = [
        {'id': 1, 'name': 'Alice', 'email': 'alice@example.com'},
        {'id': 2, 'name': 'Bob', 'email': 'bob@example.com'},
        {'id': 3, 'name': 'Charlie', 'email': 'charlie@example.com'}
    ]
    extracted_data = extract_required_keys(sample_data)
    print(extracted_data)