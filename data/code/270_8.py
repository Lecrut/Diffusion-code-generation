import sys
def process_string(input_string):
    return input_string.replace(" ", "")
if __name__ == '__main__':
    sample_input = "This is a sample string with spaces"
    try:
        result = process_string(sample_input)
        print(result)
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)