def find_smallest(list_of_integers):
    if not list_of_integers:
        return None
    return min(list_of_integers)

if __name__ == '__main__':
    sample_values = [-15, 30, -25, 40, 0]
    smallest_value = find_smallest(sample_values)
    print(smallest_value)