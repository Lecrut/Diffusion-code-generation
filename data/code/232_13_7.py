def print_growing_sequence():
    term = 2
    multipliers = [1] * 6
    for i in range(5):
        multipliers[i + 1] = round(multipliers[i] * 1.5)
    
    for multiplier in multipliers:
        print(round(term * multiplier))

if __name__ == '__main__':
    print_growing_sequence()