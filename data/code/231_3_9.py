class TupleRepeater:
    def repeat_and_flatten(self):
        result = [('X', 'Y')] * 5
        return [item for sublist in result for item in sublist]

if __name__ == '__main__':
    repeater = TupleRepeater()
    flattened_result = repeater.repeat_and_flatten()
    print(flattened_result)