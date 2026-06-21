class StreamChecker:
    def __init__(self, iterable):
        self.iterable = iter(iterable)

    @staticmethod
    def contains(element, stream_checker):
        return any(item == element for item in stream_checker.iterable)

if __name__ == '__main__':
    sample_stream = (1, 5, 2, 8, 3, 5)
    stream_checker = StreamChecker(sample_stream)
    print(f"Checking for 2: {StreamChecker.contains(2, stream_checker)}")
    print(f"Checking for 5: {StreamChecker.contains(5, stream_checker)}")
    print(f"Checking for 9: {StreamChecker.contains(9, stream_checker)}")
    print(f"Checking for 1: {StreamChecker.contains(1, stream_checker)}")
    print(f"Checking for 8: {StreamChecker.contains(8, stream_checker)}")