def generate_arithmetic_progression(start, difference, terms):
    return [start + i * difference for i in range(terms)]

if __name__ == '__main__':
    progression = generate_arithmetic_progression(5, 3, 15)
    print(progression)