def middle(seq):
    length = len(seq)
    index = length // 2
    if length % 2 == 0:
        index -= 1
    return seq[index]

assert middle([1, 2, 3]) == 2
assert middle([1, 2, 3, 4]) == 2
assert middle([10]) == 10
assert middle([1, 2]) == 1

if __name__ == '__main__':
    print(middle([10, 20, 30, 40, 50]))
    print(middle([1, 2, 3]))