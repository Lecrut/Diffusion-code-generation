def sort_three_numbers(a, b, c):
    if a > b:
        a, b = b, a
    if b > c:
        b, c = c, b
    if a > b:
        a, b = b, a
    return a, b, c

if __name__ == '__main__':
    sample_values = [5, 2, 8]
    sorted_values = sort_three_numbers(*sample_values)
    print(f"Sorted values: {sorted_values}")

    sample_values_2 = [100, 42, 34]
    sorted_values_2 = sort_three_numbers(*sample_values_2)
    print(f"Sorted values: {sorted_values_2}")

    sample_values_3 = [7, 7, 7]
    sorted_values_3 = sort_three_numbers(*sample_values_3)
    print(f"Sorted values: {sorted_values_3}")