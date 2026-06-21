def sort_reverse(a, b):
    if a > b:
        return [a, b]
    return [b, a]

if __name__ == '__main__':
    print(sort_reverse(10, 20))