class IterableChecker:
    def __init__(self, *iterables):
        self.iterables = iterables

    def is_mutually_exclusive(self):
        combined_elements = set()
        for iterable in self.iterables:
            if not isinstance(iterable, (list, tuple, set)):
                raise ValueError("All arguments must be iterables")
            current_elements = set(iterable)
            intersection = combined_elements.intersection(current_elements)
            if intersection:
                return False
            combined_elements.update(current_elements)
        return True

if __name__ == '__main__':
    checker1 = IterableChecker([1, 2, 3], [4, 5, 6], [7, 8, 9])
    print(f"Mutual Exclusivity: {checker1.is_mutually_exclusive()}")

    checker2 = IterableChecker(['a', 'b'], ['c', 'd'], ['e', 'f'])
    print(f"Mutual Exclusivity: {checker2.is_mutually_exclusive()}")

    checker3 = IterableChecker([1, 2], [2, 3], [4, 5])
    print(f"Mutual Exclusivity: {checker3.is_mutually_exclusive()}")