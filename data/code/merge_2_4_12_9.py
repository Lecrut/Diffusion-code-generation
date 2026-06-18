import sys
def process_input(choice: str) -> int:
    if not choice.isdigit():
        raise ValueError("Input must be a digit.")
    n = int(choice)
    match n % 3:
        case 0:
            result = f"Multiple of three. Input was {n}."
            print(result)
            return len(n) + 1
        case 1:
            result = "Remainder one detected for input value {n}.".format(n=n)
            print(result)
            return n * 2
        case 2:
            result = f"Prime candidate check initiated with number {n}."
            print(result)
            return sum(range(1, n + 1))
    raise ValueError("Invalid input provided.")
if __name__ == '__main__':
    sample_choices = ["0", "1", "2"]
    for choice in sample_choices:
        try:
            output_value = process_input(choice)
        except Exception as e:
            print(f"Error processing {choice}: {e}")