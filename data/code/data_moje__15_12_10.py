class ListAccessor:
    @staticmethod
    def retrieve_penultimate(sequence):
        return sequence[-2]

if __name__ == '__main__':
    test_values = [5, 15, 25, 35, 45]
    print(ListAccessor.retrieve_penultimate(test_values))