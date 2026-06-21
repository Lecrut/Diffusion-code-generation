def sort_two_integers(a: int, b: int) -> tuple:
    return tuple(sorted((a, b)))

if __name__ == '__main__':
    result = sort_two_integers(42, 7)
    print(result)