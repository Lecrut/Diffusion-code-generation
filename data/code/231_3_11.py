def repeat_and_flatten():
    pattern = ('X', 'Y')
    repeated_pattern = [pattern] * 5
    flattened_result = [item for sublist in repeated_pattern for item in sublist]
    return flattened_result

if __name__ == '__main__':
    print(repeat_and_flatten())