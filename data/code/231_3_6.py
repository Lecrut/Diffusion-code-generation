def repeat_and_validate():
    pattern = [('X', 'Y')] * 5
    if not all(isinstance(item, tuple) and len(item) == 2 for item in pattern):
        raise ValueError("Each item must be a tuple of length 2")
    
    return [item for sublist in pattern for item in sublist]

if __name__ == '__main__':
    flattened_result = repeat_and_validate()
    print(flattened_result)