def largest_of_three(a, b, c):
    largest = a
    if b > largest:
        largest = b
    if c > largest:
        largest = c
    return largest

def main():
    a = 10
    b = 15
    c = 5
    result = largest_of_three(a, b, c)
    print(f'The largest of {a}, {b}, and {c} is {result}.')
if __name__ == '__main__':
    main()