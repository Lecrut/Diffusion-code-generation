def validate_input(n):
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    return n

def generate_powers_of_two(n):
    powers = []
    for i in range(n):
        power = 1 << i
        powers.append(power)
    return powers

if __name__ == '__main__':
    try:
        num_powers = validate_input(10)
        result = generate_powers_of_two(num_powers)
        print(result)
    except ValueError as e:
        print(e)