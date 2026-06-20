class SequenceHandler:
    MIN_LENGTH = 2

    @staticmethod
    def get_first_and_last(sequence):
        if len(sequence) < SequenceHandler.MIN_LENGTH:
            raise ValueError("Sequence must contain at least two elements.")
        return sequence[0], sequence[-1]

if __name__ == '__main__':
    list_sample = [10, 20, 30, 40, 50]
    tuple_sample = (5, 15, 25, 35, 45)
    
    handler = SequenceHandler()
    
    print(f"List sample: {list_sample}")
    try:
        first_last_list = handler.get_first_and_last(list_sample)
        print(f"First and last of list: {first_last_list}")
    except ValueError as e:
        print(f"Error for list: {e}")
    
    print(f"\nTuple sample: {tuple_sample}")
    try:
        first_last_tuple = handler.get_first_and_last(tuple_sample)
        print(f"First and last of tuple: {first_last_tuple}")
    except ValueError as e:
        print(f"Error for tuple: {e}")