class LastItemUnavailable(Exception):
    def __init__(self, details):
        self.details = details
        super().__init__(details)

def check_length(sequence):
    if len(sequence) == 0:
        return False
    return True

def retrieve_tail(sequence):
    if not check_length(sequence):
        raise LastItemUnavailable("The provided sequence contains no elements")
    return sequence[len(sequence) - 1]

if __name__ == '__main__':
    items = [10, 25, 42, 99, 31]
    final_value = retrieve_tail(items)
    print(final_value)
    
    nothing = []
    try:
        retrieve_tail(nothing)
    except LastItemUnavailable as err:
        print(err.details)