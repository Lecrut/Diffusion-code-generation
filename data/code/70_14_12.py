BOUNDARY_LABELS = {
    'first': 0,
    'last': -1
}

def extract_boundaries(collection):
    if not collection:
        raise ValueError("Collection must not be empty")
    first_index = BOUNDARY_LABELS['first']
    last_index = BOUNDARY_LABELS['last']
    return collection[first_index], collection[last_index]

if __name__ == '__main__':
    sample_data = [5, 10, 15, 20, 25]
    boundary_values = extract_boundaries(sample_data)
    print(boundary_values)