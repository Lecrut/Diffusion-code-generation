class TupleRepeater:
    def __init__(self):
        self.result = ()

    def repeat_elements(self, input_tuple, k):
        for element in input_tuple:
            self.result += (element,) * k

    def get_repeated_tuple(self):
        return self.result

if __name__ == '__main__':
    repeater = TupleRepeater()
    repeater.repeat_elements((1, 2, 3), 2)
    print(repeater.get_repeated_tuple())