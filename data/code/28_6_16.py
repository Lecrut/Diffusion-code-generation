def sort_two_numbers(a, b):
    if a <= b:
        return (a, b)
    else:
        return (b, a)

if __name__ == '__main__':
    result = sort_two_numbers(15, 3)
    print(result)