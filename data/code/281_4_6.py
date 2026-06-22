def sum_of_seven_integers(a, b, c, d, e, f, g):
    numbers = [a, b, c, d, e, f, g]
    total_sum = sum(numbers)
    return total_sum

if __name__ == '__main__':
    sample_values = (3, 5, 7, 9, 11, 13, 15)
    result = sum_of_seven_integers(*sample_values)
    print(f"Sum of {sample_values}: {result}")