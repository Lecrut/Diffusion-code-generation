def consecutive_multipliers(limit):
    for i in range(1, limit + 1):
        yield i
if __name__ == '__main__':
    limit = 5
    generator = consecutive_multipliers(limit)
    results = []
    for num in generator:
        results.append(num)
    print(f"Multipliers up to {limit}: {results}")