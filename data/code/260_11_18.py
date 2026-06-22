MAX_VALUE = float('-inf')

def find_max_in_sets(*sets):
    return {set_name: max(set_values, default=MAX_VALUE) for set_name, set_values in zip("ABCDEF", sets)}

if __name__ == '__main__':
    sample_sets = (
        (10, 20, 30),
        (45, 5, 15),
        (60, 70, 80)
    )
    max_values = find_max_in_sets(*sample_sets)
    print(max_values)