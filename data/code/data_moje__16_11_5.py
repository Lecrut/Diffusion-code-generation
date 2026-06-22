class TupleExtractor:
    def __init__(self, data):
        self.data = data

    def get_first(self):
        head, *tail = self.data
        return head

    def get_rest(self):
        head, *tail = self.data
        return tuple(tail)

def extract_first_item(tup):
    extractor = TupleExtractor(tup)
    return extractor.get_first()

if __name__ == '__main__':
    sample = (99, 88, 77)
    print(extract_first_item(sample))