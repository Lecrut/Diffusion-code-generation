def sort_two_integers(a, b):
    if a <= b:
        return (a, b)
    else:
        return (b, a)

if __name__ == '__main__':
    result = sort_two_integers(5, 3)
    print(result)
    result2 = sort_two_integers(10, 10)
    print(result2)
    result3 = sort_two_integers(-1, 42)
    print(result3)