class TupleRepeater:
    def repeat_and_flatten(self):
        result = [('X', 'Y')] * 5
        flattened_result = [item for sublist in result for item in sublist]
        return flattened_result

if __name__ == '__main__':
    repeater = TupleRepeater()
    flattened_list = repeater.repeat_and_flatten()
    print(flattened_list)