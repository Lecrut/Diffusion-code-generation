class EmptyListError(Exception):
    def __init__(self, message="The list is empty"):
        self.message = message
        super().__init__(self.message)

def get_last_item(lst):
    if not lst:
        raise EmptyListError()
    return lst[-1]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    try:
        result = get_last_item(sample_list)
        print(result)
    except EmptyListError as e:
        print(e.message)

    empty_list = []
    try:
        result = get_last_item(empty_list)
        print(result)
    except EmptyListError as e:
        print(e.message)