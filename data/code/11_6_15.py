class IndexError(Exception):
    def __init__(self):
        super().__init__("The provided list is empty and has no last item.")

def get_last_element(input_list):
    if len(input_list) == 0:
        raise IndexError()
    return input_list[-1]

def process_and_display(values):
    print(get_last_element(values))

if __name__ == '__main__':
    valid_data = [10, 25, 42, 88, 150]
    process_and_display(valid_data)
    empty_data = []
    try:
        process_and_display(empty_data)
    except IndexError as error:
        print(str(error))