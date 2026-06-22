class TupleRepeater:
    REPEAT_COUNT = 5

    @staticmethod
    def repeat_and_flatten():
        pattern = [('X', 'Y')] * TupleRepeater.REPEAT_COUNT
        flattened_result = [item for sublist in pattern for item in sublist]
        return flattened_result

if __name__ == '__main__':
    result = TupleRepeater.repeat_and_flatten()
    print(result)