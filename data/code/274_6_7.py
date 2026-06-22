class ListIterator:
    def __init__(self, input_list):
        self.input_list = input_list

    @staticmethod
    def print_with_index(input_list):
        for index, item in enumerate(input_list):
            print(f"{index}: {item}")

if __name__ == '__main__':
    sample_list = ['apple', 'banana', 'cherry']
    ListIterator.print_with_index(sample_list)