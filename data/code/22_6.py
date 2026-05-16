def odd_even_checker(start, end):
    for number in range(start, end + 1):
        if number % 2 != 0:
            yield "odd"
        else:
            yield "even"
if __name__ == '__main__':
    results = list(odd_even_checker(1, 20))
    print(results)