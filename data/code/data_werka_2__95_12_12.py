def check_number(n):
    return n > 0 and n % 2 == 0 and n < 100

def process_numbers(a, b, c):
    results = []
    for num in [a, b, c]:
        if not isinstance(num, int):
            raise ValueError("Input must be an integer")
        results.append(check_number(num))
    return results

if __name__ == '__main__':
    sample_inputs = [10, 200, -5]
    output = process_numbers(*sample_inputs)
    print(output)