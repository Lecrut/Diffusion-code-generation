def repeat_and_flatten():
    pattern = [('X', 'Y')] * 5
    flattened_pattern = [item for sublist in pattern for item in sublist]
    return flattened_pattern

if __name__ == '__main__':
    sample_result = repeat_and_flatten()
    print(sample_result)