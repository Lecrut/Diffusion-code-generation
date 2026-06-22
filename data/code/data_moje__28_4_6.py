def sort_integers_reverse(a, b):
    numbers = [a, b]
    numbers.sort(reverse=True)
    return numbers

if __name__ == '__main__':
    num1 = 10
    num2 = 42
    result = sort_integers_reverse(num1, num2)
    print(result)