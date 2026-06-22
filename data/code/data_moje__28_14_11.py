def sort_two_numbers(a, b):
    return (a, b) if a <= b else (b, a)

if __name__ == '__main__':
    result = sort_two_numbers(5, 2)
    print(result)