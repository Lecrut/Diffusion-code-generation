import sys
try:
    def get_max(data):
        return max(data)
except TypeError as e:
    print(f"Input must be iterable: {e}")
    sys.exit(1)
if __name__ == '__main__':
    sample_input = [3, 5, -20.6, 'a', 7]
    try:
        result = get_max(sample_input)
        print(result)
    except Exception as e:
        if isinstance(e, TypeError):
            print(f"Error processing input type {type(sample_input).__name__}")
        else:
            raise