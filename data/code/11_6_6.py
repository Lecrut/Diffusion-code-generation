class IndexError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

def validate_sequence(seq):
    if len(seq) == 0:
        raise IndexError("Input sequence is empty")
    return True

def access_last_element(sequence):
    validate_sequence(sequence)
    return sequence[-1]

if __name__ == '__main__':
    valid_data = ["apple", "banana", "cherry", "date"]
    result = access_last_element(valid_data)
    print(result)
    empty_data = []
    try:
        access_last_element(empty_data)
    except IndexError as err:
        print(err.message)