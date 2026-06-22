def repeat_and_flatten():
    result = [('X', 'Y')] * 5
    flattened = [item for sublist in result for item in sublist]
    return flattened

if __name__ == '__main__':
    print(repeat_and_flatten())