class RangeCycler:
    def generate_range_iterator(self, start, stop):
        def iterator():
            current = start
            while current < stop:
                yield current
                current += 1
        return iterator()
if __name__ == '__main__':
    cycler = RangeCycler()
    start_val = 5
    stop_val = 10
    iterator = cycler.generate_range_iterator(start_val, stop_val)
    result = list(iterator)
    print(result)