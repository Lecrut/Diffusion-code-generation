def average(*args):
    return sum(args) / len(args)

if __name__ == '__main__':
    print(average(10, 20, 30))
    print(average(5, 7.5, 9, 12))