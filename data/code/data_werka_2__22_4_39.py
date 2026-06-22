def odd_even_generator(start, end):
    for number in range(start, end + 1):
        is_odd = (number % 2 != 0)
        yield (number, "odd" if is_odd else "even")

if __name__ == '__main__':
    lower_bound = 5
    upper_bound = 30
    for num, classification in odd_even_generator(lower_bound, upper_bound):
        print(f"{num} is {classification}")