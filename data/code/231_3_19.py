def repeat_and_flatten():
    repeated_tuples = [('X', 'Y')] * 5
    flattened_list = [item for sublist in repeated_tuples for item in sublist]
    return flattened_list

if __name__ == '__main__':
    print(repeat_and_flatten())