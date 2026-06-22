def generate_powers_of_two(n):
    powers = []
    current_power = 1
    for _ in range(n):
        powers.append(current_power)
        current_power <<= 1
    return powers

if __name__ == '__main__':
    number_of_powers = 10
    start_value = 2
    sample_values = generate_powers_of_two(start_value + number_of_powers - 1)
    result = sample_values[-number_of_powers:]
    print(result)