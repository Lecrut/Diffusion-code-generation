MAX_INTEGER_CONVERSION_ERROR = ValueError("All elements must be convertible to integers")

def extract_max_integer(str_list):
    try:
        return max(int(num) for num in str_list)
    except ValueError as e:
        raise MAX_INTEGER_CONVERSION_ERROR from e

if __name__ == '__main__':
    sample_values = ["10", "20", "30", "40"]
    print(extract_max_integer(sample_values))