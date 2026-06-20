class SequenceInspector:
    def inspect_sequence(self, seq):
        if not seq:
            return (None, None)
        return (seq[0], seq[-1])

if __name__ == '__main__':
    inspector = SequenceInspector()
    sample_list = [1, 2, 3, 4, 5]
    sample_tuple = (10, 20, 30)
    empty_list = []
    empty_tuple = ()
    print(inspector.inspect_sequence(sample_list))
    print(inspector.inspect_sequence(sample_tuple))
    print(inspector.inspect_sequence(empty_list))
    print(inspector.inspect_sequence(empty_tuple))