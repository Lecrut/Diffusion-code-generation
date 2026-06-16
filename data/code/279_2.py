class RangeCycler:
    def generate_sequence(self, start, end):
        return list(range(start, end + 1))
if __name__ == '__main__':
    cycler = RangeCycler()
    start_val = 5
    end_val = 12
    sequence = cycler.generate_sequence(start_val, end_val)
    print(sequence)