sample_values = {
    'numbers': [3.5, 2.1, 4.8, 6.7]
}

def calculate_mean(data):
    return sum(data['numbers']) / len(data['numbers'])

if __name__ == '__main__':
    result = calculate_mean(sample_values)
    print(result)