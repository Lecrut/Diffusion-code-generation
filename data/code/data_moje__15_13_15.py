def penultimate(lst):
    if len(lst) < 2:
        return None
    return lst[-2]

if __name__ == '__main__':
    print(penultimate([1, 2, 3, 4, 5]))
    print(penultimate([10]))
    print(penultimate([]))
    print(penultimate([7, 8]))
    print(penultimate([1, 2, 3]))