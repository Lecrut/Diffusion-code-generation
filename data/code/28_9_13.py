def sort_two_numbers(a, b):
    if a < b:
        return (a, b)
    else:
        return (b, a)

if __name__ == '__main__':
    num1 = 3.14
    num2 = 2.71
    sorted_pair = sort_two_numbers(num1, num2)
    print(sorted_pair)