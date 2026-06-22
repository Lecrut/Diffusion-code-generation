class ListRepeater:
    def __init__(self):
        self.base_list = [10, 20]

    def repeat_and_flatten(self, times):
        repeated_list = self.base_list * times
        return tuple(repeated_list)

if __name__ == '__main__':
    repeater = ListRepeater()
    result = repeater.repeat_and_flatten(7)
    print(result)