class EvenCounter:
    def count_evens(self, iterable):
        count = 0
        iterator = iter(iterable)
        while True:
            try:
                number = next(iterator)
                if number % 2 == 0:
                    count += 1
            except StopIteration:
                break
        return count

if __name__ == '__main__':
    counter = EvenCounter()
    sample_list = [1, 2, 3, 4, 5]
    result = counter.count_evens(sample_list)
    print(f"Number of even numbers in {sample_list}: {result}")