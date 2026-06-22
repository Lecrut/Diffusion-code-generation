import itertools

class TupleRepeater:
    def repeat_elements(self, tup, n):
        return tuple(itertools.chain.from_iterable(itertools.repeat(x, n) for x in tup))

if __name__ == '__main__':
    repeater = TupleRepeater()
    sample_tup = (1, 2, 3)
    repetition_count = 4
    result = repeater.repeat_elements(sample_tup, repetition_count)
    print(result)