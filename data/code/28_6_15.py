def compare_numbers(a, b):
    if a <= b:
        return (a, b)
    else:
        return (b, a)

if __name__ == '__main__':
    print(compare_numbers(10, 5))