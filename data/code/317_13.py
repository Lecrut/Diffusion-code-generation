class RangeCycler:
    def generate_range_iterator(self, start: int, end: int) -> iter:
        return iter(range(start, end))
if __name__ == '__main__':
    cycler = RangeCycler()
    start_val = 5
    end_val = 10
    iterator = cycler.generate_range_iterator(start_val, end_val)
    result = list(iterator)
    print(f"Generated range: {result}")