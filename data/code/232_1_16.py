def growing_sequence(limit):
    if limit < 1:
        raise ValueError("Limit must be greater than 0")
    return (x for x in range(1, limit + 1))

if __name__ == '__main__':
    try:
        for number in growing_sequence(15):
            print(number)
    except ValueError as e:
        print(e)