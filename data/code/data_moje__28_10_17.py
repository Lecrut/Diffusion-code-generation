def sort_two_integers(a, b):
    return (a, b) if a <= b else (b, a)

if __name__ == '__main__':
    result = sort_two_integers(10, 5)
    print(result)