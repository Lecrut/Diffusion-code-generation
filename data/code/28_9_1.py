def sort_two_numbers(a, b):
    if a < b:
        return [a, b]
    return [b, a]

if __name__ == '__main__':
    x = 5.7
    y = 2.3
    result = sort_two_numbers(x, y)
    print(result)