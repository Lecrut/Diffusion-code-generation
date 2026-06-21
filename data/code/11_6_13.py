class ListEmptyError(Exception):
    def __init__(self, context):
        self.context = context
        super().__init__(f"Cannot retrieve tail from {context}")

def check_sequence_length(items):
    if len(items) == 0:
        raise ListEmptyError("empty list")

def obtain_tail_value(items):
    check_sequence_length(items)
    return items[-1]

def process_test_data(input_list):
    try:
        return obtain_tail_value(input_list)
    except ListEmptyError as error:
        return str(error)

if __name__ == '__main__':
    test_numbers = [10, 25, 30, 45, 50]
    empty_numbers = []
    
    result_one = process_test_data(test_numbers)
    print(result_one)
    
    result_two = process_test_data(empty_numbers)
    print(result_two)