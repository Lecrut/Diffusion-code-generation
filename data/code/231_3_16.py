def repeat_and_flatten():
    base_pattern = ('X', 'Y')
    repeated_patterns = [base_pattern] * 5
    flattened_result = [item for sublist in repeated_patterns for item in sublist]
    return flattened_result

if __name__ == '__main__':
    print(repeat_and_flatten())