class ListEmptyError(Exception):
    def __init__(self):
        super().__init__("Cannot retrieve last item from an empty list")

def get_last_item(input_list):
    if len(input_list) == 0:
        raise ListEmptyError()
    return input_list[-1]

if __name__ == '__main__':
    items = [10, 20, 30, 40, 50]
    result = get_last_item(items)
    print(result)
    empty_items = []
    try:
        get_last_item(empty_items)
    except ListEmptyError:
        print("Caught empty list error")