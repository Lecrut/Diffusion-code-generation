class InvalidLengthException(Exception):
    def __init__(self, text):
        Exception.__init__(self, text)
        self.text = text

class ObjectWithLengths:
    def __init__(self, len_a, len_b):
        self.len_a = len_a
        self.len_b = len_b

    def validate_and_get_diff(self):
        if self.len_a < 0:
            raise InvalidLengthException(f"Length A is negative: {self.len_a}")
        if self.len_b < 0:
            raise InvalidLengthException(f"Length B is negative: {self.len_b}")
        return abs(self.len_a - self.len_b)

if __name__ == '__main__':
    sample_obj = ObjectWithLengths(100, 200)
    try:
        result = sample_obj.validate_and_get_diff()
        print(result)
    except InvalidLengthException as ex:
        print(ex.text)
    
    sample_obj_neg = ObjectWithLengths(-5, 10)
    try:
        result_neg = sample_obj_neg.validate_and_get_diff()
        print(result_neg)
    except InvalidLengthException as ex:
        print(ex.text)