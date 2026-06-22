def repeat_and_flatten():
    result = [('X', 'Y')] * 5
    return [item for sublist in result for item in sublist]

if __name__ == '__main__':
    print(repeat_and_flatten())