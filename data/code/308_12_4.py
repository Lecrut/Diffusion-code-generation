class SequenceCounter:
    def count(self, data):
        return len(data)
if __name__ == '__main__':
    counter = SequenceCounter()
    sample_list = [1, 2, 3, 4, 5]
    sample_tuple = ('a', 'b', 'c')
    sample_string = "hello"
    count1 = counter.count(sample_list)
    print(f"Count of {sample_list}: {count1}")
    count2 = counter.count(sample_tuple)
    print(f"Count of {sample_tuple}: {count2}")
    count3 = counter.count(sample_string)
    print(f"Count of {sample_string}: {count3}")