def sort_reverse(a, b):
    values = [a, b]
    values.sort(reverse=True)
    return values

if __name__ == '__main__':
    result = sort_reverse(5, 10)
    print(result)