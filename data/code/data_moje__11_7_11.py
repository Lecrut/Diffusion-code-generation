class SequenceUtils:
    @staticmethod
    def retrieve_last_item(sequence):
        iterator = reversed(sequence)
        return next(iterator)

if __name__ == '__main__':
    colors = ["red", "green", "blue", "yellow"]
    result = SequenceUtils.retrieve_last_item(colors)
    print(result)