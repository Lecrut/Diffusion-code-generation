def max_integer(lst):
    return max(lst) if lst else None

if __name__ == '__main__':
    print(max_integer([3, 5, 1, 2]))
    print(max_integer([]))