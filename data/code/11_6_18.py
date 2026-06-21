class SequenceEndError(Exception):
    def __init__(self, target_type):
        self.target_type = target_type
        super().__init__(f"Attempted to access the end of an empty {target_type}")

def check_length(collection):
    if len(collection) == 0:
        raise SequenceEndError(type(collection).__name__)
    return True

def get_final_element(collection):
    check_length(collection)
    return collection[-1]

if __name__ == '__main__':
    active_items = [42, 15, 99, 7]
    final_value = get_final_element(active_items)
    print(final_value)
    void_list = []
    try:
        get_final_element(void_list)
    except SequenceEndError as failure:
        print(failure)