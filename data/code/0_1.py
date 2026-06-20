def extract_numbers(input_string: str) -> str:
    return "".join([char for char in input_string if char.isdigit()])

if __name__ == "__main__":
    sample_text = "Order 12345 shipped on 2023-10-05 with tracking #9876543210!"
    result = extract_numbers(sample_text)
    print(result)