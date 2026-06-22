def repeat_and_flatten():
    repeated_tuples = [('X', 'Y')] * 5
    flattened_result = [item for sublist in repeated_tuples for item in sublist]
    return flattened_result

if __name__ == '__main__':
    result = repeat_and_flatten()
    print(result)