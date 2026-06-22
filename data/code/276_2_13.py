class TupleRepeater:
    def repeat_elements(self, tup, K):
        return tup * K

if __name__ == '__main__':
    repeater = TupleRepeater()
    sample_tuple = (1, 2, 3)
    times_to_repeat = 3
    repeated_tuple = repeater.repeat_elements(sample_tuple, times_to_repeat)
    print(repeated_tuple)