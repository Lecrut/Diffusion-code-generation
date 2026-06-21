class LastItemEmptyException(Exception):
    def __init__(self, item_count):
        self.item_count = item_count
        msg = "Attempted to access last item from a collection with {count} elements".format(count=item_count)
        super().__init__(msg)
        self.message = msg

def extract_final_element(collection):
    if len(collection) == 0:
        raise LastItemEmptyException(0)
    return collection[-1]

if __name__ == '__main__':
    test_list = [5, 10, 15, 20]
    print(extract_final_element(test_list))
    empty_list = []
    try:
        extract_final_element(empty_list)
    except LastItemEmptyException as e:
        print(e.message)