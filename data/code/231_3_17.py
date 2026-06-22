class TupleRepeater:
    TUPLE_TO_REPEAT = ('X', 'Y')
    REPEAT_COUNT = 5

    @staticmethod
    def repeat_and_flatten():
        result = [TupleRepeater.TUPLE_TO_REPEAT] * TupleRepeater.REPEAT_COUNT
        flattened_result = [item for sublist in result for item in sublist]
        return flattened_result

if __name__ == '__main__':
    repeater = TupleRepeater()
    repeated_flattened = repeater.repeat_and_flatten()
    print(repeated_flattened)