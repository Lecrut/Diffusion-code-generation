def extract_initial(items):
    return items[0]

def validate_collection(data):
    return isinstance(data, list) and len(data) > 0

def get_head(sequence):
    if not validate_collection(sequence):
        raise ValueError("Collection must be a non-empty list")
    return extract_initial(sequence)

if __name__ == '__main__':
    sample_values = [7, 14, 21]
    output = get_head(sample_values)
    print(output)