THIRD_INDEX = 2
SAMPLE_DATA = [99, 88, 77, 66, 55]

def retrieve_value_at_index(collection, index):
    if index < 0:
        return collection[index]
    if index >= len(collection):
        return None
    return collection[index]

if __name__ == '__main__':
    target_index = THIRD_INDEX
    output = retrieve_value_at_index(SAMPLE_DATA, target_index)
    print(output)