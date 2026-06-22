def repeat_and_flatten():
    result = [('X', 'Y')] * 5
    flattened_result = [item for sublist in result for item in sublist]
    return flattened_result

if __name__ == '__main__':
    print(repeat_and_flatten())