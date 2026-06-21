def _ensure_sequence(value):
    if not isinstance(value, (list, tuple, set)):
        raise TypeError("Expected a sequence type")
    if len(value) == 0:
        raise ValueError("Sequence must not be empty")
    return value

def retrieve_head(collection):
    validated = _ensure_sequence(collection)
    return validated[0]

if __name__ == '__main__':
    items = ['alpha', 'beta', 'gamma']
    output = retrieve_head(items)
    print(output)