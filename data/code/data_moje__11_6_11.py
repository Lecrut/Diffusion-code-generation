class LastItemRetrievalError(Exception):
    def __init__(self, data_type):
        self.data_type = data_type
        message = f"Unable to retrieve the last item from an empty {data_type}."
        super().__init__(message)

def is_collection_empty(collection):
    return len(collection) == 0

def get_last_entry(data):
    if is_collection_empty(data):
        raise LastItemRetrievalError(type(data).__name__)
    return data[-1]

if __name__ == '__main__':
    working_list = [42, 17, 99, 3]
    print(get_last_entry(working_list))
    
    empty_list = []
    try:
        result = get_last_entry(empty_list)
        print(result)
    except LastItemRetrievalError as error:
        print(error)