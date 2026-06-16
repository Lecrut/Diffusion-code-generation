class RangeCycler:
    def generate_sequence(self, start, end):
        sequence = list(range(start, end + 1))
        return sequence
if __name__ == '__main__':
    cycler = RangeCycler()
    start_val = 5
    end_val = 12
    result = cycler.generate_sequence(start_val, end_val)
    print(result)