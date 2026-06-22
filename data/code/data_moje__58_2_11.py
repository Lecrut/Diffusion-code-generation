def count_evens_bitwise(start, end):
    if start > end:
        return 0

    def count_evens_up_to(n):
        if n < 0:
            return 0
        return (n >> 1) + 1
    return count_evens_up_to(end) - count_evens_up_to(start - 1)
if __name__ == '__main__':
    result1 = count_evens_bitwise(0, 10)
    print(result1)
    result2 = count_evens_bitwise(1, 10)
    print(result2)
    result3 = count_evens_bitwise(-5, 5)
    print(result3)
    result4 = count_evens_bitwise(10, 0)
    print(result4)
    result5 = count_evens_bitwise(2, 2)
    print(result5)
    result6 = count_evens_bitwise(3, 3)
    print(result6)