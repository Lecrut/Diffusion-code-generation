class BooleanNegator:
    TRUE_CONSTANT = True
    FALSE_CONSTANT = False
    EXPECTED_LIST_LENGTH = 1

    def __init__(self):
        self.notation_map = {
            self.TRUE_CONSTANT: self.FALSE_CONSTANT,
            self.FALSE_CONSTANT: self.TRUE_CONSTANT
        }

    def negate(self, input_list):
        if not isinstance(input_list, list):
            raise ValueError("Input must be a list")
        if len(input_list) != self.EXPECTED_LIST_LENGTH:
            raise ValueError(f"List must contain exactly {self.EXPECTED_LIST_LENGTH} element")
        
        element = input_list[0]
        if not isinstance(element, bool):
            raise ValueError("Element must be a boolean")
            
        return self.notation_map[element]

if __name__ == '__main__':
    negator = BooleanNegator()
    sample_list = [True]
    result = negator.negate(sample_list)
    print(result)