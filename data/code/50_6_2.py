def absolute_difference_generator(*args):
    if not args:
        return
    previous_value = args[0]
    yield abs(previous_value - args[1])
    for i in range(1, len(args) - 1):
        yield abs(args[i] - args[i+1])
if __name__ == '__main__':
    numbers = [10, 5, 8, 2, 15]
    for diff in absolute_difference_generator(*numbers):
        print(diff)