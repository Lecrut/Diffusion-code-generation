def sort_two(a, b):
    return (a, b) if a <= b else (b, a)

if __name__ == '__main__':
    print(sort_two(5, 3))