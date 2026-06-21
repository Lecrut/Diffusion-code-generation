def calculate_average(*args):
    return float(sum(args)) / len(args)

if __name__ == '__main__':
    print(calculate_average(10, 20, 30, 40, 50))