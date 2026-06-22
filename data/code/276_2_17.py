class TupleRepeater:

    def __init__(self):
        self.tuple = ()

    def set_tuple(self, new_tuple):
        self.tuple = new_tuple

    def repeat_elements(self, times):
        result = ()
        for element in self.tuple:
            result += (element,) * times
        return result
if __name__ == '__main__':
    repeater = TupleRepeater()
    repeater.set_tuple((1, 2, 3))
    repeated_tuple = repeater.repeat_elements(3)
    print(repeated_tuple)