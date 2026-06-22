class ListChecker:
    _type_registry = {
        list: "sequence",
        tuple: "sequence",
        str: "string"
    }

    def get_extremes(self, data):
        if not isinstance(data, (list, tuple, str)):
            raise ValueError("Input must be a sequence")
        if len(data) == 0:
            raise ValueError("Sequence cannot be empty")
        return (data[0], data[-1])

if __name__ == '__main__':
    checker = ListChecker()
    sample_data = [5, 15, 25, 35, 45]
    first, last = checker.get_extremes(sample_data)
    print((first, last))