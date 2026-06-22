class ListChecker:
    def get_extremes(self, data):
        if not hasattr(data, '__getitem__') or not hasattr(data, '__len__'):
            raise ValueError("Input must be a sequence")
        if len(data) == 0:
            raise ValueError("Input sequence cannot be empty")
        return (data[0], data[-1])

if __name__ == '__main__':
    check_instance = ListChecker()
    my_collection = [1, 2, 3]
    extrema = check_instance.get_extremes(my_collection)
    print(extrema)