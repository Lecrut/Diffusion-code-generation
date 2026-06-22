def count_evens(iterable):
    count = 0
    iterator = iter(iterable)
    while True:
        try:
            element = next(iterator)
            if element % 2 == 0:
                count += 1
        except StopIteration:
            break
    return count

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print(f"Number of even numbers in {sample_list}: {count_evens(sample_list)}")