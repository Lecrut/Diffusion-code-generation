def sort_ascending(a, b):
    return (a, b) if a <= b else (b, a)

if __name__ == '__main__':
    print(sort_ascending(5, 3))