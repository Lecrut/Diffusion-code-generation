NUM_TUPLES = ((1, 2), (3, 4), (5, 6))

def calculate_total(tuples):
    return sum(sum(t) for t in tuples)

def count_elements(tuples):
    return sum(len(t) for t in tuples)

def average_of_tuples(tuples):
    total = calculate_total(tuples)
    count = count_elements(tuples)
    return total / count if count > 0 else 0

if __name__ == '__main__':
    print(average_of_tuples(NUM_TUPLES))