import sys
def process_string(input_string):
    try:
        result = input_string.replace(" ", "")
        print(result)
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)
if __name__ == '__main__':
    sample_input = "This is a sample string with spaces"
    process_string(sample_input)