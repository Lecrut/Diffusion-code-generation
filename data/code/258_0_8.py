def calculate_averages(data):
    averages = {'first': 0, 'second': 0}
    count_first = count_second = 0
    
    for pair in data:
        if len(pair) >= 2:
            averages['first'] += pair[0]
            count_first += 1
            averages['second'] += pair[1]
            count_second += 1
    
    if count_first > 0:
        averages['first'] /= count_first
    if count_second > 0:
        averages['second'] /= count_second
    
    return averages

if __name__ == '__main__':
    sample_data = [
        (10, 5),
        (20, 15),
        (30, 25)
    ]
    
    result = calculate_averages(sample_data)
    print(f"Average of first elements: {result['first']}")
    print(f"Average of second elements: {result['second']}")