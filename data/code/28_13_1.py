def sort_two_numbers(a, b):
    if a > b:
        return (b, a)
    return (a, b)

if __name__ == '__main__':
    result = sort_two_numbers(5, 3)
    print(result)