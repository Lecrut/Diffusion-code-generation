def odd_even_generator(start, end):
    for num in range(start, end + 1):
        yield f"{num} is {'even' if num % 2 == 0 else 'odd'}"

if __name__ == '__main__':
    start = 1
    end = 20
    for result in odd_even_generator(start, end):
        print(result)