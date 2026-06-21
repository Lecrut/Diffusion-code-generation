def extract_boundary_indices(data):
    metadata = {
        'label': 'boundary',
        'type': 'tuple',
        'description': 'first and last element of sequence'
    }
    if not isinstance(data, (list, tuple)):
        raise ValueError("Unsupported type")
    if len(data) < 1:
        raise ValueError("Empty sequence")
    first = data[0]
    last = data[-1]
    result = {
        'metadata': metadata,
        'values': (first, last),
        'count': len(data)
    }
    return result

if __name__ == '__main__':
    values = [42, 99, 17, 64, 8]
    output = extract_boundary_indices(values)
    print(output['values'])