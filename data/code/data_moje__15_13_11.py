def penultimate(lst):
    if lst is None or len(lst) < 2:
        return None
    return lst[-2]

if __name__ == '__main__':
    print(penultimate([1, 2, 3, 4]))
    print(penultimate([1]))
    print(penultimate([]))