def sort_two_integers(a, b):
    return (a, b) if a <= b else (b, a)

if __name__ == '__main__':
    result = sort_two_integers(5, 3)
    print(result)
    result = sort_two_integers(10, 20)
    print(result)
    result = sort_two_integers(-1, -5)
    print(result)
    result = sort_two_integers(0, 0)
    print(result)
    result = sort_two_integers(100, 1)
    print(result)