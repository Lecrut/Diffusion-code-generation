def count_evens(start, end):
    def count_upto(n):
        if n < 0:
            return -count_upto(-n) - 1
        return (n // 2) + (1 if n % 2 == 0 else 0) - (1 if n < 0 else 0)
    if start > end:
        return 0
    return count_upto(end) - count_upto(start - 1)

if __name__ == '__main__':
    result = count_evens(3, 15)
    print(result)