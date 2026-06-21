class EmptyListException(Exception):
    def __init__(self):
        super().__init__("Attempted to access last item of an empty list")

def get_last_item(lst):
    if len(lst) == 0:
        raise EmptyListException()
    return lst[-1]

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50]
    last_val = get_last_item(sample_values)
    print(last_val)

    empty_values = []
    try:
        get_last_item(empty_values)
    except EmptyListException as e:
        print(str(e))