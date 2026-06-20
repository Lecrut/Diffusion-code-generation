class SequenceChecker:
    def check_sequence(self, seq):
        if not isinstance(seq, (list, tuple)):
            raise ValueError("Input must be a list or tuple.")
        return (seq[0], seq[-1])

if __name__ == '__main__':
    checker = SequenceChecker()
    sample_list = [1, 2, 3, 4, 5]
    sample_tuple = (10, 20, 30)
    empty_list = []
    empty_tuple = ()
    invalid_input = "not a sequence"
    
    print(checker.check_sequence(sample_list))
    print(checker.check_sequence(sample_tuple))
    print(checker.check_sequence(empty_list))
    print(checker.check_sequence(empty_tuple))