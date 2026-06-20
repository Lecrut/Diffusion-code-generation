class SequenceChecker:
    def check_sequence(self, seq):
        if seq:
            return (seq[0], seq[-1])
        else:
            return (None, None)

if __name__ == '__main__':
    checker = SequenceChecker()
    sample_list = [1, 2, 3, 4, 5]
    sample_tuple = (10, 20, 30)
    empty_list = []
    empty_tuple = ()
    print(checker.check_sequence(sample_list))
    print(checker.check_sequence(sample_tuple))
    print(checker.check_sequence(empty_list))
    print(checker.check_sequence(empty_tuple))