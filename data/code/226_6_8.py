SEQUENCE = [1, 2, 3]
COUNT_LIMIT = 50

def repeating_sequence_generator():
    count = 0
    while count < COUNT_LIMIT:
        for item in SEQUENCE:
            yield item
            count += 1
            if count >= COUNT_LIMIT:
                return

if __name__ == '__main__':
    gen = repeating_sequence_generator()
    result = [next(gen) for _ in range(COUNT_LIMIT)]
    print(result)