def evens_upto(n):
    return (n + 1) // 2

def count_evens(start, end):
    if start > end:
        return 0
    return evens_upto(end) - evens_upto(start - 1)

if __name__ == '__main__':
    print(count_evens(1, 10))
    print(count_evens(2, 2))
    print(count_evens(1, 1))
    print(count_evens(5, 5))
    print(count_evens(6, 6))
    print(count_evens(0, 0))
    print(count_evens(-5, 5))