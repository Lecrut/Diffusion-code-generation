def sort_asc(a, b):
    return (a, b) if a < b else (b, a)

if __name__ == '__main__':
    print(sort_asc(5, 2))