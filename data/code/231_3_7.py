def repeat_and_flatten():
    patterns = [('X', 'Y')] * 5
    flattened_list = [item for sublist in patterns for item in sublist]
    return flattened_list

if __name__ == '__main__':
    result = repeat_and_flatten()
    print(result)