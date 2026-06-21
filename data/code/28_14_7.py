def sort_two(a, b):
    return (a, b) if a <= b else (b, a)

if __name__ == '__main__':
    result = sort_two(3, 1)
    print(result)