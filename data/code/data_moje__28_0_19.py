def sort_two_numbers(a, b):
    if a < b:
        return (a, b)
    else:
        return (b, a)

if __name__ == '__main__':
    x = 10
    y = 5
    result = sort_two_numbers(x, y)
    print(result)