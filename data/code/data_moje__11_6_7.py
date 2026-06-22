class EmptyListError(Exception):
    def __init__(self, message="The list is empty"):
        super().__init__(message)

def get_last_item(lst):
    if not lst:
        raise EmptyListError()
    return lst[-1]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    result = get_last_item(sample_list)
    print(result)

    try:
        get_last_item([])
    except EmptyListError as e:
        print(str(e))