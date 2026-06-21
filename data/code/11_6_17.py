class ListIsEmptyError(Exception):
    def __init__(self, detail="No elements to retrieve"):
        self.detail = detail
        super().__init__(self.detail)

def safe_tail(items):
    if not items:
        raise ListIsEmptyError()
    return items[len(items) - 1]

if __name__ == '__main__':
    data_source = [10, 20, 30, 40, 50]
    last_value = safe_tail(data_source)
    print(last_value)
    vacant_source = []
    try:
        safe_tail(vacant_source)
    except ListIsEmptyError as error:
        print(error.detail)