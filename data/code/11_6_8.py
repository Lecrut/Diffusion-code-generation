class LastItemError(Exception):
    def __init__(self, msg):
        self.msg = msg
        super().__init__(msg)

def get_last_item(lst):
    if len(lst) == 0:
        raise LastItemError("List is empty")
    return lst[-1]

if __name__ == '__main__':
    data = [10, 20, 30]
    result = get_last_item(data)
    print(result)
    empty_data = []
    try:
        get_last_item(empty_data)
    except LastItemError as e:
        print(e.msg)