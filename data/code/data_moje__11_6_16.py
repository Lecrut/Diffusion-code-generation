class EmptyListError(Exception):
    def __init__(self):
        super().__init__("The list is empty")

def get_last_item(items):
    if not items:
        raise EmptyListError()
    return items[-1]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40]
    empty_list = []
    print(get_last_item(sample_list))
    try:
        print(get_last_item(empty_list))
    except EmptyListError:
        print("Caught exception: Empty list")