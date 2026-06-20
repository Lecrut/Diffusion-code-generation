def sum_range(start, end):
    return (end - start + 1) * (start + end) // 2
if __name__ == '__main__':
    print(sum_range(1, 10))