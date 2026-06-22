def generate_arithmetic_progression(start=5, difference=3, terms=15):
    return [start + i * difference for i in range(terms)]

if __name__ == '__main__':
    print(generate_arithmetic_progression())