class ThirdItemAccessor:
    INDEX_OFFSET = 2

    @staticmethod
    def retrieve(collection):
        if len(collection) > ThirdItemAccessor.INDEX_OFFSET:
            return collection[ThirdItemAccessor.INDEX_OFFSET]
        return None

if __name__ == '__main__':
    accessor = ThirdItemAccessor()
    full_sequence = [5, 15, 25, 35]
    short_sequence = [1, 2]
    print(accessor.retrieve(full_sequence))
    print(accessor.retrieve(short_sequence))