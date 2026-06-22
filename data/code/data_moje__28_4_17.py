def sort_reverse(a, b):
    result = [a, b]
    result.sort(reverse=True)
    return result

if __name__ == '__main__':
    x = 10
    y = 5
    print(sort_reverse(x, y))