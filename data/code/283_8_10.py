class TupleCounter:
    def count_non_tuples(self, items):
        non_tuple_count = 0
        for item in items:
            if not isinstance(item, tuple):
                non_tuple_count += 1
        return non_tuple_count

if __name__ == '__main__':
    counter = TupleCounter()
    sample_list = ["apple", "banana", (1, 2), "kiwi", {"a": 1}, (3, 4)]
    result = counter.count_non_tuples(sample_list)
    print(result)