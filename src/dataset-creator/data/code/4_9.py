def compute_sum(input_line):
    try:
        numbers = input_line.split()
        if len(numbers) != 3:
            raise ValueError("Expected three numbers.")
        nums = [int(n) for n in numbers]
        return sum(nums)
    except ValueError as e:
        return f"Error processing input: {e}"
if __name__ == '__main__':
    sample_input = "10 20 30"
    result = compute_sum(sample_input)
    print(result)