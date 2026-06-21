def sort_two_numbers(a, b):
    if a <= b:
        return [a, b]
    return [b, a]
if __name__ == '__main__':
    result1 = sort_two_numbers(5, 3)
    print(result1)
    result2 = sort_two_numbers(10, 10)
    print(result2)
    result3 = sort_two_numbers(-1, 4)
    print(result3)
    result4 = sort_two_numbers(0, -5)
    print(result4)
    result5 = sort_two_numbers(100, 50)
    print(result5)