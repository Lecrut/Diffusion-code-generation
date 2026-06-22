def repeat_and_flatten():
    pattern = [('X', 'Y')] * 5
    return [item for sublist in pattern for item in sublist]

if __name__ == '__main__':
    flattened_result = repeat_and_flatten()
    print(flattened_result)