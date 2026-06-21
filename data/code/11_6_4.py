class EmptyListError(Exception):
    def __init__(self):
        super().__init__("Cannot retrieve last item from an empty list")

def get_last_item(data):
    if len(data) == 0:
        raise EmptyListError()
    return data[len(data) - 1]

if __name__ == '__main__':
    items = [10, 20, 30]
    print(get_last_item(items))
    try:
        get_last_item([])
    except EmptyListError as e:
        print(str(e))