def sort_descending(a, b):
    if a > b:
        return [a, b]
    return [b, a]

if __name__ == '__main__':
    result = sort_descending(10, 3)
    print(result)
    result2 = sort_descending(5, 20)
    print(result2)
    result3 = sort_descending(-1, -5)
    print(result3)
    result4 = sort_descending(0, 0)
    print(result4)