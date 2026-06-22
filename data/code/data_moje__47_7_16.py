def mean(lst):
    if not lst:
        raise ValueError("Empty list")
    return sum(lst) / len(lst)

if __name__ == '__main__':
    data = [1, 2, 3, 4, 5]
    print(mean(data))