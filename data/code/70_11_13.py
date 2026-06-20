class EndpointPrinter:
    @staticmethod
    def print_first_and_last(strings):
        try:
            first = next(iter(strings))
            last = next(reversed(strings))
        except StopIteration:
            first, last = None, None
        return first, last

if __name__ == '__main__':
    sample_lists = [
        ['apple', 'banana', 'cherry'],
        ['hello', 'world'],
        [],
        ['single']
    ]
    
    for lst in sample_lists:
        first, last = EndpointPrinter.print_first_and_last(lst)
        print(f"First: {first}, Last: {last}")