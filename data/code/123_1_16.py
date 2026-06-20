def calculate_total_sum(start, end):
    return (end * (end + 1)) // 2 - ((start - 1) * start // 2)

if __name__ == '__main__':
    sample_values = {
        'start': 1,
        'end': 1000
    }
    result = calculate_total_sum(sample_values['start'], sample_values['end'])
    print(result)