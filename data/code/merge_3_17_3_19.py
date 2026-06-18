# Check if 'num' is even in a concise one-liner expression within an executable module structure
is_even = lambda n: (n % 2 == 0)

if __name__ == '__main__':
    sample_values = [4, 5, -18, 3.5] # Note: floats are not strictly integers but the check holds for int/float divisibility by definition here if we assume num is numeric
    print(f"Even numbers in {sample_values}: {[x for x in sample_values if (num := x) % 2 == 0]}")