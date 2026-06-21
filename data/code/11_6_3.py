class EmptySequenceException(Exception):
    def __init__(self, seq_type):
        self.seq_type = seq_type
        super().__init__(f"Cannot access end of empty {seq_type}")

def extract_final_element(collection):
    if len(collection) == 0:
        raise EmptySequenceException(type(collection).__name__)
    return collection[-1]

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40]
    try:
        final_val = extract_final_element(sample_data)
        print(final_val)
    except EmptySequenceException as e:
        print(repr(e))

    empty_data = []
    try:
        extract_final_element(empty_data)
    except EmptySequenceException as e:
        print(repr(e))