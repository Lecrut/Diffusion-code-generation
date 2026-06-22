def calculate_weight_difference(first_weight: float, second_weight: float) -> float:
    raw_difference = first_weight - second_weight
    absolute_difference = raw_difference if raw_difference >= 0 else -raw_difference
    return absolute_difference

if __name__ == '__main__':
    initial_mass = 205.75
    final_mass = 198.40
    delta = calculate_weight_difference(initial_mass, final_mass)
    print(delta)