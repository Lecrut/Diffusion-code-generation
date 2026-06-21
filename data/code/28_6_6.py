def sort_two_numbers(a, b):
    if a < b:
        return (a, b)
    else:
        return (b, a)

if __name__ == '__main__':
    result = sort_two_numbers(5, 2)
    print(result)
    result2 = sort_two_numbers(-3, 7)
    print(result2)
    result3 = sort_two_numbers(10, 10)
    print(result3)