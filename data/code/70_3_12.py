def first_last(iterable):
    return (iterable[0], iterable[-1]) if iterable else None
if __name__ == '__main__':
    print(first_last([1, 2, 3, 4]))
    print(first_last('hello'))
    print(first_last([]))