class ListChecker:
    def get_extremes(self, data):
        if len(data) == 0:
            raise ValueError("Sequence must contain at least one element")
        first_element = data[0]
        last_element = data[-1]
        return (first_element, last_element)

if __name__ == '__main__':
    test_values = [99, 12, 77, 4, 88]
    checker_instance = ListChecker()
    extremes = checker_instance.get_extremes(test_values)
    print(extremes)