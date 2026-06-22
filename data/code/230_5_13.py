class LengthSet:
    def __init__(self, string_set):
        self.lengths = sorted({len(s) for s in string_set})

    def get_lengths(self):
        return self.lengths

if __name__ == '__main__':
    sample_set = {"apple", "banana", "cherry", "date"}
    length_set_instance = LengthSet(sample_set)
    print("Unique lengths:", length_set_instance.get_lengths())