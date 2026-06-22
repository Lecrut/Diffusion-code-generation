def find_the_middle_value_among_three_summary(a, b, c):
    values = [a, b, c]
    if len(values) != 3:
        raise ValueError("Exactly three values are required")
    
    unique_values = list(set(values))
    if len(unique_values) != 3:
        raise ValueError("All three values must be unique")
    
    return sorted(unique_values)[1]

if __name__ == '__main__':
    a = 10
    b = 5
    c = 20
    middle_value = find_the_middle_value_among_three_summary(a, b, c)
    print(middle_value)