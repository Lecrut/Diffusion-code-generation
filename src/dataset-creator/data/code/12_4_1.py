def check_odd_generator():
    return (n for n in range(10) if n % 2 != 0)
if __name__ == '__main__':
    gen = check_odd_generator()
    count = sum(True for _ in gen)
    print(f"Total odd numbers found: {count}")