def range_iterator(func):
    def wrapper(start, step):
        for i in range(start, start + step):
            yield i
    return wrapper
@range_iterator
def iterate_range(start, step):
    for i in range(start, start + step):
        yield i
if __name__ == '__main__':
    print("Testing iteration from 0 to 4 with step 1:")
    for number in iterate_range(0, 1):
        print(number)
    print("-" * 20)
    print("Testing iteration from 2 to 8 with step 2:")
    for number in iterate_range(2, 2):
        print(number)
    print("-" * 20)
    print("Testing iteration from 10 to 15 with step -2:")
    for number in iterate_range(10, -2):
        print(number)