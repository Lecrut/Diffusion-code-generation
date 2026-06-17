class RangeCycler:
    def generate_range_iterator(self, start, stop):
        return iter(range(start, stop))
if __name__ == '__main__':
    cycler = RangeCycler()
    start_val = 1
    stop_val = 6
    iterator = cycler.generate_range_iterator(start_val, stop_val)
    result = list(iterator)
    print(result)