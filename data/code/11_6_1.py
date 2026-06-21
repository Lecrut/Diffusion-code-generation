class CollectionEmptyError(Exception):
    def __init__(self, source):
        self.source = source
        super().__init__(f"Cannot retrieve last item from empty {source}")

def validate_non_empty(data):
    if not data:
        raise CollectionEmptyError("list")

def fetch_tail(data):
    validate_non_empty(data)
    return data[-1]

if __name__ == '__main__':
    test_set = [100, 200, 300, 400, 500]
    print(fetch_tail(test_set))
    empty_set = []
    try:
        result = fetch_tail(empty_set)
        print(result)
    except CollectionEmptyError as error:
        print(error)