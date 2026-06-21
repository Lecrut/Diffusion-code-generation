class ListChecker:
    def __init__(self):
        self.empty_message = "Sequence cannot be empty"

    def get_extremes(self, sequence):
        if len(sequence) == 0:
            raise ValueError(self.empty_message)
        first_item = sequence[0]
        last_item = sequence[-1]
        return (first_item, last_item)

if __name__ == '__main__':
    data = [1, 2, 3, 4, 5]
    checker = ListChecker()
    extremes = checker.get_extremes(data)
    print(extremes)