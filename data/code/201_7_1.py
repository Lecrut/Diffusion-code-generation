def avg(lst):
    return sum(lst) / len(lst) if lst else 0

if __name__ == '__main__':
    print(avg([1, 2, 3, 4, 5]))
    print(avg([]))