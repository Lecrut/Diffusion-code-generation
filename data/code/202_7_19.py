def find_largest_integer(start, end):
    return max(range(start, end + 1))

if __name__ == '__main__':
    start = 5
    end = 20
    print(find_largest_integer(start, end))