def generate_sequence(start, end):
    sequence = list(range(start, end + 1))
    return sequence

if __name__ == '__main__':
    start_value = 1
    end_value = 10
    result = generate_sequence(start_value, end_value)
    print(result)