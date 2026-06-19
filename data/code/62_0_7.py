def fetch_second_element(sequence):
    return sequence[1]

if __name__ == '__main__':
    sample_data = {
        'fruits': ['apple', 'banana', 'cherry'],
        'numbers': [5, 15, 25, 35],
        'colors': ['red', 'green', 'blue']
    }
    
    second_fruit = fetch_second_element(sample_data['fruits'])
    print(second_fruit)