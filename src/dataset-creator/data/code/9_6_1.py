def calculate_average(*args):
    if not args:
        return 0
    return sum(args) / len(args)
if __name__ == '__main__':
    print(calculate_average(1, 2, 3))
    print(calculate_average(10, 20, 30, 40))
    print(calculate_average(5.5, 10.5, 15.0))
    print(calculate_average())
    print(calculate_average(7))