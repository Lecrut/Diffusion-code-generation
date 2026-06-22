TILE = ('X', 'Y')
REPEAT_COUNT = 5

def repeat_and_flatten():
    result = [TILE] * REPEAT_COUNT
    flattened_result = [item for sublist in result for item in sublist]
    return flattened_result

if __name__ == '__main__':
    print(repeat_and_flatten())