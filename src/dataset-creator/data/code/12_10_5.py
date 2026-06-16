def is_odd(n):
    return n & 1 != 0
def main():
    numbers = [5, -3, 42, -7]
    for num in numbers:
        if is_odd(num):
            print(f"{num} is odd")
        else:
            print(f"{num} is even")
if __name__ == '__main__':
    main()