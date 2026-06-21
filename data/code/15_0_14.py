SECOND_TO_LAST_INDEX = -2

def retrieve_penultimate(data):
    return data[SECOND_TO_LAST_INDEX]

if __name__ == '__main__':
    collection = [1, 2, 3, 4, 5]
    output = retrieve_penultimate(collection)
    print(output)