def compute_negation(data):
    if not data:
        raise ValueError("List must contain exactly one element")
    element = data[0]
    if element is True:
        return False
    if element is False:
        return True
    raise ValueError("Element must be a boolean")
if __name__ == '__main__':
    sample_data = [False]
    print(compute_negation(sample_data))