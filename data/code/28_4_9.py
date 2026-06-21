def sort_integers_reverse(a, b):
    values = [a, b]
    values.sort(reverse=True)
    return values

if __name__ == '__main__':
    result = sort_integers_reverse(10, 5)
    print(result)