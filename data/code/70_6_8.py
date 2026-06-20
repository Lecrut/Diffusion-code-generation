class SequenceHandler:
    def __init__(self, sequence):
        self.sequence = sequence

    def get_first_and_last(self):
        if len(self.sequence) < 2:
            raise ValueError("Sequence must contain at least two elements.")
        return (self.sequence[0], self.sequence[-1])

if __name__ == '__main__':
    list_sample = [10, 20, 30, 40, 50]
    handler = SequenceHandler(list_sample)
    try:
        first_last_list = handler.get_first_and_last()
        print(f"First and last of list: {first_last_list}")
    except ValueError as e:
        print(f"Error for list: {e}")

    tuple_sample = (5, 15, 25, 35, 45)
    handler = SequenceHandler(tuple_sample)
    try:
        first_last_tuple = handler.get_first_and_last()
        print(f"First and last of tuple: {first_last_tuple}")
    except ValueError as e:
        print(f"Error for tuple: {e}")

    single_element = [99]
    handler = SequenceHandler(single_element)
    try:
        result_single = handler.get_first_and_last()
    except ValueError as e:
        print(f"Error for single element: {e}")