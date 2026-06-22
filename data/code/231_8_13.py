class ListRepeater:
    REPEAT_COUNT = 7

    @staticmethod
    def repeat_list(input_list):
        return input_list * ListRepeater.REPEAT_COUNT

    @staticmethod
    def flatten_and_convert_to_tuple(repeated_list):
        return tuple(flatten(repeated_list))

def flatten(lst):
    for elem in lst:
        if isinstance(elem, list):
            yield from flatten(elem)
        else:
            yield elem

if __name__ == '__main__':
    input_list = [10, 20]
    repeated_list = ListRepeater.repeat_list(input_list)
    result = ListRepeater.flatten_and_convert_to_tuple(repeated_list)
    print(result)