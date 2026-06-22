EMPTY_LIST_THRESHOLD = 0

class ListChecker:
    def get_extremes(self, data):
        if len(data) <= EMPTY_LIST_THRESHOLD:
            raise ValueError("Input sequence is empty")
        first_item = data[0]
        last_item = data[-1]
        return (first_item, last_item)

if __name__ == '__main__':
    sample_data = [5, 15, 25, 35, 45]
    checker = ListChecker()
    print(checker.get_extremes(sample_data))