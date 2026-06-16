class SequenceCounter:
    def count(self, data):
        return len(data)
if __name__ == '__main__':
    counter = SequenceCounter()
    sample_list = [1, 2, 3, 4, 5]
    sample_tuple = ('a', 'b', 'c')
    sample_string = "hello"
    sample_empty = []
    print(f"Count of {sample_list}: {counter.count(sample_list)}")
    print(f"Count of {sample_tuple}: {counter.count(sample_tuple)}")
    print(f"Count of '{sample_string}': {counter.count(sample_string)}")
    print(f"Count of {sample_empty}: {counter.count(sample_empty)}")