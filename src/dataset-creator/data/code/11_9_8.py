def consecutive_multipliers(limit):
    for i in range(1, limit + 1):
        yield i
if __name__ == '__main__':
    limit = 5
    results = list(consecutive_multipliers(limit))
    print(f"Consecutive integers up to {limit}: {results}")