LIST_CHUNK_SIZE = 10**6

def concatenate_lists(list_x, list_y):
    if not isinstance(list_x, list) or not isinstance(list_y, list):
        raise ValueError("Both arguments must be lists")
    
    result = list_x[:]
    start_index = len(result)
    for chunk in [list_y[i:i+LIST_CHUNK_SIZE] for i in range(0, len(list_y), LIST_CHUNK_SIZE)]:
        result[start_index:start_index+len(chunk)] = chunk
        start_index += len(chunk)
    
    return result

if __name__ == '__main__':
    sample_list1 = list(range(LIST_CHUNK_SIZE))
    sample_list2 = list(range(LIST_CHUNK_SIZE, 2 * LIST_CHUNK_SIZE))
    try:
        print(concatenate_lists(sample_list1, sample_list2))
    except ValueError as e:
        print(e)