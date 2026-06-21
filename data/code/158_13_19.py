if __name__ == '__main__':
    start = 1
    end = 20
    step = 2

    if not isinstance(start, int) or not isinstance(end, int) or not isinstance(step, int):
        raise ValueError("All parameters must be integers.")

    for num in range(start, end + 1, step):
        print(num)