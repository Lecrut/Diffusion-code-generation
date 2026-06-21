class LastEntryExtractor:
    EMPTY_MSG = "Cannot extract from empty dictionary"

    @staticmethod
    def get_last_pair(data):
        if not data:
            raise ValueError(LastEntryExtractor.EMPTY_MSG)
        last_key = next(reversed(data))
        return (last_key, data[last_key])

if __name__ == '__main__':
    sample = {"x": 100, "y": 200, "z": 300}
    print(LastEntryExtractor.get_last_pair(sample))