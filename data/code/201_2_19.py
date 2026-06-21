def calculate_average(*args):
    if not args:
        return 0
    return sum(args) / len(args)

if __name__ == '__main__':
    print(calculate_average(10, 20, 30))
    print(calculate_average(5.5, 4.5, 6.5))