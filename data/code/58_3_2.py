def count_evens(start, end):
    start += 1 if start % 2 != 0 else 0
    end -= 1 if end % 2 != 0 else 0
    if start > end:
        return 0
    return (end - start) // 2 + 1

if __name__ == '__main__':
    result = count_evens(1, 10)
    print(result)