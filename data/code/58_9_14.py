def count_evens(start, end):
    if not isinstance(start, int) or not isinstance(end, int):
        raise TypeError("Start and end must be integers")
    if start > end:
        raise ValueError("Start must be less than or equal to end")
    def count_upto(n):
        return n // 2
    return count_upto(end) - count_upto(start - 1)

if __name__ == '__main__':
    result = count_evens(1, 10)
    print(result)