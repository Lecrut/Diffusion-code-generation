class ListChecker:
    MIN_VALID_LENGTH = 1

    def __init__(self, sequence):
        self._elements = list(sequence)

    def get_first_and_last(self):
        length = len(self._elements)
        if length < self.MIN_VALID_LENGTH:
            raise ValueError("List must contain at least one element")
        
        first_index = 0
        last_index = length - 1
        
        first_element = self._elements[first_index]
        last_element = self._elements[last_index]
        
        return first_element, last_element

if __name__ == '__main__':
    sample_values = [5, 12, 8, 19, 3]
    checker = ListChecker(sample_values)
    result = checker.get_first_and_last()
    print(result)