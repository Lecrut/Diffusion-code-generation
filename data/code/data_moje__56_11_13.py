def generate_multiplication_table(number, max_multiplier=10):
    lines = [f"{number} x {i} = {number * i}" for i in range(1, max_multiplier + 1)]
    return "\n".join(lines)

if __name__ == '__main__':
    target_number = 7
    print(generate_multiplication_table(target_number))