def calculate_averages(pairs):
    averages = {}
    for pair in pairs:
        if len(pair) != 2:
            continue
        first, second = pair
        averages['first'] = (averages.get('first', 0) * averages.get('count', 0) + first) / (averages.get('count', 0) + 1)
        averages['second'] = (averages.get('second', 0) * averages.get('count', 0) + second) / (averages.get('count', 0) + 1)
        averages['count'] = averages.get('count', 0) + 1
    return averages

if __name__ == '__main__':
    pairs = [
        (10, 20),
        (5, 15),
        (8, 2),
        (12, 30)
    ]
    result = calculate_averages(pairs)
    print(f"Average of the first numbers: {result['first']}")
    print(f"Average of the second numbers: {result['second']}")