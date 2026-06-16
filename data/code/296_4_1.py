def simulate_ratio_change(numerator, denominator, amount, steps):
    current_numerator = numerator
    current_denominator = denominator
    for _ in range(steps):
        current_numerator += amount
        current_denominator += amount
    return current_numerator, current_denominator
if __name__ == '__main__':
    initial_numerator = 10
    initial_denominator = 20
    fixed_amount = 3
    num_steps = 5
    final_numerator, final_denominator = simulate_ratio_change(initial_numerator, initial_denominator, fixed_amount, num_steps)
    print(f"Initial Ratio: {initial_numerator}/{initial_denominator}")
    print(f"Fixed Amount Added: {fixed_amount} over {num_steps} steps")
    print(f"Final Numerator: {final_numerator}")
    print(f"Final Denominator: {final_denominator}")
    print(f"Final Ratio: {final_numerator}/{final_denominator}")