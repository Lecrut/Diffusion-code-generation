def find_the_middle_value_among_three_rank_samples(a, b, c):
    if not all(isinstance(x, (int, float)) for x in [a, b, c]):
        raise ValueError("All inputs must be numbers")
    
    values = sorted([a, b, c])
    return values[1]

if __name__ == '__main__':
    try:
        middle_value = find_the_middle_value_among_three_rank_samples(3, 1, 2)
        print(middle_value)
    except ValueError as e:
        print(e)